# %%
import numpy as np
import gym
import gym_organism

env = gym.make("Organism-v0")

env.reset() # reset environment to a new, random state

q_table = np.zeros([env.observation_space.n, env.action_space.n])
print('hey there')

"""Training the agent"""
print("How many generations ?")
gen = int(input())

import random
from time import sleep
from IPython.display import clear_output

# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.1
gen_done = False
for j in range(gen):
    
    print("Gen : ", j+1)
    time_taken = 0
    total_penalty = 0
    # For plotting metrics
    all_epochs = []
    all_penalties = []
    frames = []
    times_eaten = 0
    for i in range(1, 101):
        epochs, penalties, reward, = 0, 0, 0
        done = False
        state = env.reset()
        while epochs<20 and not done:
            if random.uniform(0, 1) < epsilon:
                action = env.action_space.sample() # Explore action space
            else:
                action = np.argmax(q_table[state]) # Exploit learned values

            next_state, reward, done, info = env.step(action)

            old_value = q_table[state, action]
            next_max = np.max(q_table[next_state])

            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[state, action] = new_value

            if reward == -10:
                penalties += 1

            frames.append({
            'frame': env.render(mode='ansi'),
            'state': state,
            'action': action,
            'reward': reward
            }
        )

#             state = next_state

#             epochs += 1

#         if i % 100 == 0:
#             clear_output(wait=True)
#             print(f"Episode: {i}")
#         time_taken += epochs
#     print(f"Total time in this generation is : {time_taken}")
#     print("Training finished.\n")
            state = next_state

            epochs += 1
#         print(done)
        if done:
            times_eaten+=1
            gen_done = True
        if i % 100 == 0:
            print(f"Episode: {i}")
        time_taken += epochs
        total_penalty += penalties

#     final_frames.append(frames)
    print(f"Total time in this generation is : {time_taken}, average time taken per episode of generation is : {time_taken/i}")
    print(f"Total penalty : {total_penalty} and average penalty : {total_penalty/100}")
    print(f"The number of times the organism ate : {times_eaten}")
    print("Training finished.\n")



# %%

def print_frames(frames):
    for i, frame in enumerate(frames):
        clear_output(wait=True)
        print(frame['frame'])
        print(f"Timestep: {i + 1}")
        print(f"State: {frame['state']}")
        print(f"Action: {frame['action']}")
        print(f"Reward: {frame['reward']}")
        sleep(.1)

print_frames(frames)


# %%


# %%


# %%
