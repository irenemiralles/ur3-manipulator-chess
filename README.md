\# UR3 Manipulator Chess



Autonomous pick-and-sort system with a Universal Robots UR3e arm: the robot picks one of three chess-piece prisms at random, shows it, and moves it to a final position only if it is the king. The joint configurations are computed in MATLAB with numerical inverse kinematics, and the arm is controlled from Python by sending URScript commands through a TCP/IP socket.

Practice (Inverse kinematics with numerical methods) of the Introduction to Robotics course, Bachelor's Degree in Artificial Intelligence, UPC.



\## Authors

\- Irene Miralles Ortega

\- Marti Andreu



\## How it works

1\. The robot starts at the initial joint configuration and opens the gripper.

2\. It picks one of the three pieces at random (positions stored as joint configurations) and closes the gripper.

3\. It moves the piece to a display position and asks the user in the console whether it is the king (`si`/`no`). Automatic recognition was not possible, as computer vision had not been covered yet.

4\. If it is the king, the robot follows a straight-line path (5 intermediate points) to the final position and finishes.

5\. If it is not, the robot puts the piece back, opens the gripper and picks again.



\## Files

| File | Description |

|------|-------------|

| `ur3\_chess.py` | Main script: opens a socket to the robot (port 30002), sends `movej` trajectories and gripper scripts |

| `pinza10UR3.py` | URScript that closes the gripper |

| `pinza40UR3.py` | URScript that opens the gripper |

| `inverse\_kinematics.mlx` | MATLAB live script: forward kinematics (DH), geometric Jacobian and numerical inverse kinematics (pseudoinverse and transpose methods, with quaternions) |



\## Requirements

\- UR3e robot with an OnRobot gripper

\- Python 3 (standard library only: `socket`, `time`, `random`)

\- MATLAB (for the live script)



\## Run

1\. Set the robot IP in `ur3\_chess.py` (`HOST`).

2\. Keep the gripper scripts in the same folder as `ur3\_chess.py`.

3\. Run:

```bash

python ur3\_chess.py

```

