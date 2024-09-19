// Lấy tham chiếu đến canvas và các nút
const canvas = document.getElementById("pendulumCanvas");
const ctx = canvas.getContext("2d");

const networkCanvas = document.getElementById("networkCanvas");
const networkCtx = networkCanvas.getContext("2d");

const saveButton = document.getElementById("saveButton");
const loadButton = document.getElementById("loadButton");

let isDragging = false;  // Trạng thái kéo thả
let mouseX = 60;  // Vị trí chuột trên trục X

// Các thông số vật lý của con lắc và giỏ
const g = 9.81; // Gia tốc trọng trường
let cartX = canvas.width / 2; // Vị trí của giỏ
let cartVelocity = 0;
let pendulumAngle = Math.PI / 4; // Góc ban đầu của con lắc (radians)
let pendulumAngularVelocity = 0;
const pendulumLength = 150; // Chiều dài con lắc
const cartWidth = 50;
const cartHeight = 30;
const mass = 1; // Khối lượng của con lắc

// Cấu hình các hành động và trạng thái
const actions = [-10, -5, 0, 5, 10]; // Các hành động có thể thực hiện (lực tác động)

// Số lần lặp qua dữ liệu để huấn luyện
const epochs = 10000;

// Dữ liệu đầu vào mẫu và đầu ra mong muốn
const trainingData = [
    {
        inputs: [0.1, 300, 0.05, 0.02, 1], // [pendulumAngle, cartX, pendulumAngularVelocity, cartVelocity, mass]
        target: [0.5] // Lực mong muốn
    },
    {
        inputs: [-0.2, 200, -0.03, -0.01, 1],
        target: [-0.5]
    },

    // Tình huống con lắc hơi lệch phải, giỏ ở giữa, vận tốc góc nhỏ
    {
        inputs: [0.1, 300, 0.05, 0.02, 1], // [pendulumAngle, cartX, pendulumAngularVelocity, cartVelocity, mass]
        target: [0.5] // Lực mong muốn
    },
    // Tình huống con lắc lệch trái, giỏ lệch trái, vận tốc góc lớn hơn
    {
        inputs: [-0.2, 200, -0.03, -0.01, 1],
        target: [-0.5]
    },
    // Tình huống con lắc lệch mạnh về bên phải, giỏ lệch về phải, tốc độ giỏ nhanh
    {
        inputs: [0.5, 350, 0.1, 0.3, 1],
        target: [0.8]
    },
    // Con lắc lệch trái, giỏ ở giữa, vận tốc góc rất nhỏ
    {
        inputs: [-0.1, 300, -0.01, 0, 1],
        target: [-0.2]
    },
    // Con lắc ở góc lớn hơn, giỏ ở đầu trái, vận tốc lớn
    {
        inputs: [-0.4, 100, -0.05, 0.05, 1],
        target: [-1.0]
    },
    // Con lắc thẳng đứng, giỏ ở giữa, không có vận tốc
    {
        inputs: [0, 300, 0, 0, 1],
        target: [0]
    },
    // Con lắc lệch phải, giỏ lệch trái, vận tốc góc vừa phải
    {
        inputs: [0.2, 150, 0.03, -0.2, 1],
        target: [0.3]
    },
    // Con lắc lệch trái, giỏ ở giữa, vận tốc góc lớn
    {
        inputs: [-0.5, 300, -0.08, 0.1, 1],
        target: [-0.7]
    },
    // Tình huống giỏ và con lắc đều lệch về bên trái
    {
        inputs: [-0.3, 200, -0.04, -0.15, 1],
        target: [-0.6]
    },
    // Tình huống giỏ lệch về phải, con lắc lệch bên phải
    {
        inputs: [0.4, 400, 0.06, 0.1, 1],
        target: [0.9]
    },
    // Tình huống con lắc và giỏ ở giữa với khối lượng khác
    {
        inputs: [0, 300, 0, 0, 1.5], // Thay đổi khối lượng
        target: [0]
    },
    // Con lắc lệch trái mạnh với khối lượng khác
    {
        inputs: [-0.3, 250, -0.07, -0.05, 1.2],
        target: [-0.4]
    },
    // Con lắc lệch phải nhẹ, khối lượng lớn hơn
    {
        inputs: [0.15, 330, 0.02, 0.03, 2],
        target: [0.2]
    },
    // Tình huống giỏ đang di chuyển nhanh sang phải và con lắc hơi lệch phải
    {
        inputs: [0.2, 350, 0.05, 0.5, 1],
        target: [0.6]
    },
    // Giỏ di chuyển nhanh sang trái, con lắc lệch trái
    {
        inputs: [-0.3, 250, -0.06, -0.5, 1],
        target: [-0.6]
    },
    // Giỏ đứng yên, con lắc lệch trái nhẹ
    {
        inputs: [-0.1, 300, -0.02, 0, 1],
        target: [-0.2]
    },
    // Thêm nhiều mẫu dữ liệu vào đây để mô phỏng các tình huống khác nhau
];

// Tạo neural network để điều khiển hệ thống
const network = new BackpropNetwork({
    inputNodes: 5, // Góc của con lắc, vị trí giỏ, tốc độ góc, tốc độ giỏ, khối lượng
    hiddenNodes: 6,
    outputNodes: 1, // Lực áp dụng lên giỏ
    createAllConnections: true
});

// Hàm huấn luyện
function trainNetwork() {
    for (let epoch = 0; epoch < epochs; epoch++) {
        let totalError = 0;
        for (const data of trainingData) {
            // Đặt đầu vào
            network.setInputs(data.inputs);
            network.calculate();

            // Lan truyền ngược để cập nhật trọng số
            network.setTargetData([data.target]);
            network.backpropagate();

            // Tính sai số
            const error = Math.abs(data.target[0] - network.getNode("OUTPUT", 0).value);
            totalError += error;
        }

        if (epoch % 100 === 0) {
            console.log(`Epoch: ${epoch}, Total Error: ${totalError}`);
        }
    }
}

// Hàm lưu trọng số vào file JSON
function saveNetworkWeights() {
    const networkData = {
        nodes: {},
        connections: {}
    };

    // Lưu các giá trị của nodes
    for (const nodeID in network.nodes) {
        networkData.nodes[nodeID] = {
            value: network.nodes[nodeID].value,
            bias: network.nodes[nodeID].bias
        };
    }

    // Lưu các trọng số của connections
    for (const connectionID in network.connections) {
        networkData.connections[connectionID] = {
            in: network.connections[connectionID].in,
            out: network.connections[connectionID].out,
            weight: network.connections[connectionID].weight
        };
    }

    // Chuyển dữ liệu thành chuỗi JSON
    const networkJSON = JSON.stringify(networkData);

    // Tạo tên file dựa trên ngày giờ hiện tại
    const now = new Date();
    const fileName = `network_weights_${now.getFullYear()}_${String(now.getMonth() + 1).padStart(2, '0')}_${String(now.getDate()).padStart(2, '0')}_`
        + `${String(now.getHours()).padStart(2, '0')}_${String(now.getMinutes()).padStart(2, '0')}_${String(now.getSeconds()).padStart(2, '0')}.json`;

    // Tạo blob và lưu file
    const blob = new Blob([networkJSON], { type: 'application/json' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    // link.download = 'network_weights.json';
    link.download = fileName;
    link.click();
}

// Hàm nạp trọng số mạng từ JSON
function loadNetworkWeights(networkJSON) {
    const data = JSON.parse(networkJSON);

    // Nạp giá trị của nodes
    for (const nodeID in data.nodes) {
        network.nodes[nodeID].value = data.nodes[nodeID].value;
        network.nodes[nodeID].bias = data.nodes[nodeID].bias;
    }

    // Nạp trọng số của connections
    for (const connectionID in data.connections) {
        network.connections[connectionID].weight = data.connections[connectionID].weight;
    }
}

// Sử dụng Fetch API để tải tệp JSON từ server
function fetchAndLoadWeights() {
    fetch('network_weights.json')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Weights loaded:', data);
            loadNetworkWeights(JSON.stringify(data));
        })
        .catch(error => console.error('Error loading JSON:', error));
}

// Hàm vẽ giỏ và con lắc lên canvas
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Vẽ giỏ
    ctx.fillStyle = "#0000ff";
    ctx.fillRect(cartX, canvas.height - cartHeight, cartWidth, cartHeight);

    // Vẽ con lắc
    const pendulumX = cartX + cartWidth / 2 + pendulumLength * Math.sin(pendulumAngle);
    const pendulumY = canvas.height - cartHeight - pendulumLength * Math.cos(pendulumAngle);

    ctx.beginPath();
    ctx.moveTo(cartX + cartWidth / 2, canvas.height - cartHeight);
    ctx.lineTo(pendulumX, pendulumY);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(pendulumX, pendulumY, 10, 0, 2 * Math.PI);
    ctx.fillStyle = "#ff0000";
    ctx.fill();
}

// Sự kiện chuột: bắt đầu kéo giỏ
canvas.addEventListener('mousedown', function (event) {
    const rect = canvas.getBoundingClientRect();
    mouseX = event.clientX - rect.left;

    // Kiểm tra nếu chuột đang ở trên giỏ
    if (mouseX > cartX && mouseX < cartX + cartWidth) {
        isDragging = true;
    }
});

// Sự kiện chuột: kéo giỏ
canvas.addEventListener('mousemove', function (event) {
    if (isDragging) {
        const rect = canvas.getBoundingClientRect();
        mouseX = event.clientX - rect.left;

        // Cập nhật vị trí của giỏ theo chuột
        cartX = mouseX - cartWidth / 2;

        // Giới hạn giỏ trong biên của canvas
        if (cartX < 0) cartX = 0;
        if (cartX > canvas.width - cartWidth) cartX = canvas.width - cartWidth;

        draw();  // Vẽ lại khi đang kéo giỏ
    }
});

// Định nghĩa DQNAgent
class DQNAgent {
    constructor() {
        this.memory = [];
        this.gamma = 0.95;    // Discount rate
        this.epsilon = 1.0;   // Exploration rate
        this.epsilon_min = 0.01;
        this.epsilon_decay = 0.995;
        this.learning_rate = 0.001;

        this.model = this.buildModel();  // Neural network model
    }

    // Xây dựng mạng neural Q
    buildModel() {
        // Mạng neural dự đoán giá trị Q cho mỗi hành động
        const network = new BackpropNetwork({
            inputNodes: 4,  // [pendulumAngle, pendulumAngularVelocity, cartX, cartVelocity]
            hiddenNodes: 24,
            outputNodes: 5, // 5 hành động (lực tác động)
            createAllConnections: true
        });
        return network;
    }

    // Chọn hành động dựa trên chính sách epsilon-greedy
    act(state) {
        if (Math.random() < this.epsilon) {
            // Chọn hành động ngẫu nhiên (exploration)
            return Math.floor(Math.random() * actions.length); // Có 5 hành động
        } else {
            // Chọn hành động tốt nhất từ mạng neural (exploitation)
            this.model.setInputs(state);
            this.model.calculate();
            const qValues = [];
            for (let i = 0; i < actions.length; i++) {
                qValues.push(this.model.getNode("OUTPUT", i).value);
            }
            return qValues.indexOf(Math.max(...qValues));  // Trả về hành động có Q-value cao nhất
        }
    }

    // Lưu trải nghiệm vào bộ nhớ
    remember(state, action, reward, nextState, done) {
        this.memory.push({ state, action, reward, nextState, done });
        // Giữ bộ nhớ không quá 2000 trải nghiệm
        if (this.memory.length > 2000) {
            this.memory.shift();
        }
    }

    // Huấn luyện mạng neural bằng cách sử dụng các mẫu từ bộ nhớ
    replay(batchSize) {
        const batch = [];
        for (let i = this.memory.length - 1; i >= 0 && batch.length < batchSize; i--) {
            batch.push(this.memory[i]);
        }

        for (const { state, action, reward, nextState, done } of batch) {
            // Tính giá trị mục tiêu
            let target = reward;
            if (!done) {
                this.model.setInputs(nextState);
                this.model.calculate();
                const futureRewards = [];
                for (let i = 0; i < actions.length; i++) {
                    futureRewards.push(this.model.getNode("OUTPUT", i).value);
                }
                target += this.gamma * Math.max(...futureRewards);
            }

            // Đặt mục tiêu cho hành động đã chọn
            this.model.setInputs(state);
            this.model.calculate();
            const currentQ = [];
            for (let i = 0; i < actions.length; i++) {
                currentQ.push(this.model.getNode("OUTPUT", i).value);
            }
            currentQ[action] = target; // Cập nhật Q-value cho hành động đã chọn

            // Đặt dữ liệu mục tiêu và huấn luyện mạng
            this.model.setMultipleNodeValues(
                actions.reduce((acc, act, idx) => {
                    acc[`OUTPUT:${idx}`] = currentQ[idx];
                    return acc;
                }, {})
            );
            this.model.backpropagate();
        }

        // Giảm epsilon (giảm khám phá khi agent học tốt hơn)
        if (this.epsilon > this.epsilon_min) {
            this.epsilon *= this.epsilon_decay;
        }
    }

    // Dự đoán giá trị Q cho một trạng thái nhất định
    predictQ(state) {
        this.model.setInputs(state);
        this.model.calculate();
        const qValues = [];
        for (let i = 0; i < actions.length; i++) {
            qValues.push(this.model.getNode("OUTPUT", i).value);
        }
        return qValues;
    }
}

// Khởi tạo agent
const agent = new DQNAgent();

// Hàm khởi tạo môi trường
function resetEnvironment() {
    pendulumAngle = (Math.random() - 0.5) * Math.PI / 6; // Góc ngẫu nhiên từ -30 đến 30 độ
    pendulumAngularVelocity = 0;
    cartX = canvas.width / 2 + (Math.random() - 0.5) * 50; // Vị trí giỏ ngẫu nhiên gần giữa
    cartVelocity = 0;

    return [pendulumAngle, pendulumAngularVelocity, cartX, cartVelocity];
}

// Hàm cập nhật môi trường
function step(action) {
    const force = actions[action]; // Lực được chọn bởi DQN

    // Cập nhật vận tốc và góc con lắc
    const angularAcceleration = (g * Math.sin(pendulumAngle) + Math.cos(pendulumAngle) * (-force - mass * pendulumLength * pendulumAngularVelocity * pendulumAngularVelocity * Math.sin(pendulumAngle))) / (pendulumLength * (4 / 3 - mass * Math.cos(pendulumAngle) * Math.cos(pendulumAngle) / (mass + 1)));
    pendulumAngularVelocity += angularAcceleration * 0.02; // Giả sử timestep = 0.02
    pendulumAngle += pendulumAngularVelocity * 0.02;

    // Cập nhật vận tốc và vị trí giỏ
    cartVelocity += force / (mass + 1) * 0.02;
    cartX += cartVelocity * 0.02;

    // Giới hạn giỏ trong biên của canvas
    if (cartX < 0) {
        cartX = 0;
        cartVelocity = 0;
    }
    if (cartX > canvas.width - cartWidth) {
        cartX = canvas.width - cartWidth;
        cartVelocity = 0;
    }

    // Tính phần thưởng
    const reward = -Math.abs(pendulumAngle); // Phần thưởng càng gần giá trị 0 thì càng tốt

    // Kiểm tra nếu trạng thái đã kết thúc
    const done = Math.abs(pendulumAngle) > Math.PI / 2; // Nếu con lắc nghiêng quá nhiều thì kết thúc

    const nextState = [pendulumAngle, pendulumAngularVelocity, cartX, cartVelocity];
    return { nextState, reward, done };
}

// Hàm huấn luyện agent
async function trainAgent() {
    const episodes = 1000;  // Số tập huấn luyện
    const batchSize = 32;  // Kích thước batch để replay

    for (let episode = 0; episode < episodes; episode++) {
        let state = resetEnvironment();
        let done = false;
        let totalReward = 0;

        while (!done) {
            // Chọn hành động từ agent
            const action = agent.act(state);

            // Thực hiện hành động và lấy phản hồi từ môi trường
            const { nextState, reward, done: doneFlag } = step(action);

            // Lưu trải nghiệm vào bộ nhớ
            agent.remember(state, action, reward, nextState, doneFlag);

            // Cập nhật trạng thái
            state = nextState;
            totalReward += reward;

            // Nếu đã thu thập đủ trải nghiệm, bắt đầu replay
            if (agent.memory.length > batchSize) {
                agent.replay(batchSize);
            }

            if (doneFlag) {
                console.log(`Episode ${episode} ended with total reward: ${totalReward.toFixed(2)}, Epsilon: ${agent.epsilon.toFixed(3)}`);
            }
        }
    }

    // Sau khi huấn luyện xong, lưu trọng số
    saveNetworkWeights();
}

// Sự kiện chuột: thả giỏ
canvas.addEventListener('mouseup', function () {
    if (isDragging) {
        isDragging = false;
        cartVelocity = 0;  // Đặt lại tốc độ giỏ khi thả
    }
});

// Tạo một NetworkVisualizer để vẽ nodes và connections
const visualizer = new NetworkVisualizer({
    canvas: "networkCanvas",
    nodeRadius: 15,
    nodeColor: "blue",
    positiveConnectionColor: "green",
    negativeConnectionColor: "red",
    connectionStrokeModifier: 2
});

// Hàm để vẽ mạng neural lên canvas
function drawNetwork() {
    visualizer.drawNetwork(network);
}

// Hàm cập nhật vẽ lại các tham số của các node lên canvas
function drawNodeParameters() {
    const fontSize = 12;
    networkCtx.font = `${fontSize}px Arial`;
    networkCtx.textAlign = "center";
    networkCtx.textBaseline = "middle";

    // Duyệt qua từng node và vẽ các tham số lên
    for (const nodeID in network.nodes) {
        const node = network.getNodeByID(nodeID);
        const location = visualizer.nodeLocations[nodeID]; // Lấy vị trí của node

        // Kiểm tra nếu node và vị trí tồn tại
        if (node && location) {
            networkCtx.fillText(`Value: ${node.value.toFixed(2)}`, location.x, location.y);

            // Chỉ hiển thị bias nếu node có thuộc tính bias
            if (typeof node.bias !== 'undefined') {
                networkCtx.fillText(`Bias: ${node.bias.toFixed(2)}`, location.x, location.y + fontSize);
            } else {
                networkCtx.fillText(`Bias: N/A`, location.x, location.y + fontSize);
            }
        }
    }
}

// Gán sự kiện cho nút Save
saveButton.addEventListener('click', function () {
    saveNetworkWeights();  // Lưu trọng số mạng sau khi huấn luyện
});

// Gán sự kiện cho nút Load
loadButton.addEventListener('click', function () {
    fetchAndLoadWeights();  // Tải và nạp trọng số từ tệp JSON
});

// Hàm tính toán các lực tác động và cập nhật vị trí
function update() {
    if(!isDragging){

    }
    
    // Lấy dữ liệu đầu vào cho neural network
    network.setInputs([pendulumAngle, cartX, pendulumAngularVelocity, cartVelocity, mass]);
    network.calculate();

    // Neural network đưa ra lực áp dụng lên giỏ
    const force = network.getNode("OUTPUT", 0).value * 10 - 5;

    // Cập nhật các giá trị vật lý dựa trên lực
    const angularAcceleration = (g * Math.sin(pendulumAngle)) / pendulumLength;
    pendulumAngularVelocity += angularAcceleration;
    pendulumAngle += pendulumAngularVelocity;

    // Cập nhật vị trí của giỏ
    cartVelocity += force;
    cartX += cartVelocity;

    // Giới hạn giỏ trong biên của canvas
    if (cartX < 0) cartX = 0;
    if (cartX > canvas.width - cartWidth) cartX = canvas.width - cartWidth;

    // Vẽ lại mọi thứ
    draw();
}

// Chỉnh sửa vòng lặp để vẽ các tham số bên trong các node
function gameLoop() {
    update();
    drawNetwork();
    // drawNodeParameters(); // Vẽ tham số bên trong các node
    requestAnimationFrame(gameLoop);
}

// trainNetwork();

// Bắt đầu vòng lặp
gameLoop();
