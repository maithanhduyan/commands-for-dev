import gymnasium as gym

# Tạo môi trường Pendulum-v1 với render_mode
env = gym.make('Pendulum-v1', render_mode='human')

# Đặt lại môi trường để bắt đầu
observation, info = env.reset()

for _ in range(1000):
    # Chọn hành động ngẫu nhiên
    action = env.action_space.sample()

    # Thực hiện hành động và nhận về các giá trị
    observation, reward, done, truncated, info = env.step(action)

    # Kiểm tra nếu môi trường kết thúc
    if done or truncated:
        observation, info = env.reset()

    # Hiển thị môi trường
    env.render()

env.close()
