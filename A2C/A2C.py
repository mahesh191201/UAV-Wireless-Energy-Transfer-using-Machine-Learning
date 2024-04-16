import gym
import gym_foo
import numpy as np
import math
from stable_baselines3 import A2C
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
env = gym.make('foo-v0')

n_actions = env.action_space.shape[-1]

model = A2C("MlpPolicy", env, learning_rate=0.0001, verbose=1, tensorboard_log="./A2C_SingleUT_Two_tensorboard/")
model.learn(total_timesteps=410000, log_interval=10)
model.save("a2c_SingleUT_Two")
env = model.get_env()

del model # remove to demonstrate saving and loading

model = A2C.load("a2c_SingleUT_Two")

obs = env.reset()
R = 0
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    R += rewards
    if dones==True:
        break
        
    env.render()
print(R)