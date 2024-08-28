import gymnasium as gym

# Tạo môi trường CartPole-v1
env = gym.make('CartPole-v1', render_mode='human')

# Đặt lại môi trường để bắt đầu
observation, info = env.reset()

for _ in range(100000):
    env.render()  # Hiển thị môi trường

    # Chọn hành động ngẫu nhiên
    action = env.action_space.sample()

    # Thực hiện hành động và nhận về các giá trị
    observation, reward, done, truncated, info = env.step(action)

    # Kiểm tra nếu môi trường kết thúc
    if done:
        observation, info = env.reset()

env.close()
