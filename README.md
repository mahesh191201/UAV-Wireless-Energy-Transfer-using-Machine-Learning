
# Project Title

Wireless Energy Transfer for UAV using Machine Learning


## Introduction

![App Screenshot](https://github.com/mahesh191201/UAV-Wireless-Energy-Transfer-using-Machine-Learning/blob/main/Screenshots/project-diagram.jpg?raw=true)

Unmanned Aerial Vehicles (UAVs), commonly known as drones, have become integral to various industries, including surveillance, delivery, agriculture, and disaster management. UAVs mounted with base stations can enable temporary communication at the time of natural disasters and assist ground users. However, the limited flight endurance of UAVs due to their small batteries remains a significant challenge, to overcome this, wireless energy transfer (WET) has emerged as a solution. The proposed system utilizes a ground-based wireless power transmitter to transmit energy to UAVs in flight. To tackle this issue, we will use a technique of machine learning, called reinforcement learning combined with deep learning known as deep reinforcement learning to maximize the energy transfer process and ensure seamless coordination between the transmitter and UAVs. The UAV is trained using a reinforcement learning algorithm to collect power from the environment by keeping track of transmission parameters, such as frequency, power level, and beam direction, based on real-time flight data, environmental conditions, and energy consumption patterns. By continuously learning from feedback during flights, the agent adapts to changing scenarios, thus enhancing the overall energy transfer efficiency. The previous work in this area has implemented a reinforcement learning algorithm Deep Deterministic Policy Gradient (DDPG) and collected only 30.4% energy. Therefore, we plan to improve the performance of the agent and maximize the energy by implementing state-of-the-art reinforcement learning algorithms. In conclusion, UAV Wireless energy transfer is a novel work that addresses the drawback of limited capacity batteries in UAVs in a unique way and has immense future scope.
## Proposed System
A2C algorithm:

![App Screenshot](https://github.com/mahesh191201/UAV-Wireless-Energy-Transfer-using-Machine-Learning/blob/main/Screenshots/a2c.png?raw=true)

A2C which stands for Advantage Actor-Critic, is a powerful deep reinforcement learning algorithm that combines the ideas of policy gradients (Actor) and value estimation (Critic) to learn effective policies for decision-making in environments with discrete or continuous action spaces. A2C is an extension of the more basic Advantage Actor-Critic algorithm, aiming to improve its stability and sample efficiency. Actor-Critic Architecture: A2C employs an actor-critic architecture, where two 
neural networks are used:

Actor: The actor network learns a policy, which is a probability distribution over actions given states. It estimates the best action to take in a given state.

Critic: The critic network learns a value function V(s), which estimates the expected cumulative reward (value) of being in a given state. It evaluates the 
goodness of states.

Advantage Estimation: A2C introduces the notion of advantage, which measures how good a particular action is compared to the average action taken in a given state.

Policy Gradient Updates: A2C updates the parameters of the actor network using policy gradient methods. The objective is to maximize the expected cumulative reward by adjusting the parameters of the policy network in the direction that 
increases the probability of good actions and decreases the probability of bad actions.

Value Function Updates: A2C updates the parameters of the critic network by minimizing the mean squared error between the estimated value function V(s) and the discounted cumulative rewards obtained from the environment.


## Result
![App Screenshot](https://github.com/mahesh191201/UAV-Wireless-Energy-Transfer-using-Machine-Learning/blob/main/Screenshots/result_graph.png?raw=true)

-> Graph showing episode vs Reward

![App Screenshot](https://github.com/mahesh191201/UAV-Wireless-Energy-Transfer-using-Machine-Learning/blob/main/Screenshots/result.png?raw=true)

-> Final result 

After implementin the A2C algorithm for our problem, we successfully achieved a 65% energy whereas the DDPG only collected 30.4%. Thus in our case the A2C algorithm beats DDPG. 



