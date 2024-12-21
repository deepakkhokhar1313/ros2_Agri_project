i want to do an major project
my goal will be: I want to make make an mobile robotic arm for an farm field of dragon fruit. My goal is that robot to roam in the farm field to reach to each dragon fruit plant to identifies leaves, fruits and harvest fruits using robotic arm.
you should make the project file structure for me. You should also give me the project architecture in visualizing way to me.
along with this write the whole project code for me including ros2 and robot model and world model file code.
technologies that I want to use:
ros2 framework to control robot like navigation etc
python programing language in ros2
I want to train robotic arm to harvest fruit using RL
I want autonomous navigation of robot in my local environment of farm.


Archtecture:
dragonfruit_farm_robot/
├── src/
│   ├── arm_control/
│   │   ├── arm_control/  # Package dir
│   │   │   ├── arm_controller.py
│   │   │   ├── arm_rl_training.py
│   │   │   ├── arm_action_server.py
│   │   │   ├── arm_utils.py
│   │   │   └── __init__.py
│   │   ├── package.xml
│   │   └── setup.py
│   ├── navigation/
│   │   ├── navigation/ # Package dir
│   │   │   ├── navigation_node.py
│   │   │   ├── path_planning.py
│   │   │   ├── localization.py
│   │   │   ├── map_server.py
│   │   │   └── __init__.py
│   │   ├── package.xml
│   │   └── setup.py
│   ├── perception/
│   │   ├── perception/ # Package dir
│   │   │   ├── image_processing.py
│   │   │   ├── object_detection.py
│   │   │   ├── data_collection.py
│   │   │   ├── camera_calibration.py
│   │   │   └── __init__.py
│   │   ├── package.xml
│   │   └── setup.py
│   ├── core/
│   │   ├── core/ # Package dir
│   │   │   ├── robot_control.py
│   │   │   ├── state_machine.py
│   │   │   ├── parameters.py
│   │   │   └── __init__.py
│   │   ├── package.xml
│   │   └── setup.py
│   ├── utilities/
│   │   ├── utilities/ # Package dir
│   │   │   ├── ros_utils.py
│   │   │   ├── math_utils.py
│   │   │   └── __init__.py
│   │   ├── package.xml
│   │   └── setup.py
│   ├── launch/
│   │   ├── robot_launch.py
│   │   ├── simulation_launch.py
│   │   └── __init__.py
│   ├── urdf/
│   │   ├── dragon_robot.urdf.xacro
│   │   ├── dragon_robot.gazebo
│   │   └── __init__.py
│   └── world/
│       ├── dragon_farm.world
│       └── __init__.py
├── data/
│   ├── training_data/
│   └── __init__.py
├── config/
│   ├── navigation_config.yaml
│   ├── perception_config.yaml
│   ├── arm_config.yaml
│   └── __init__.py
├── requirements.txt
├── README.md
└── setup.py