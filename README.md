# RI-HEVNAA
 Real-time Interrupt-driven Hemispheric Emulated von Neumann Agent Architecture
The architecture we've designed, the Real-time Interrupt-driven Hemispheric Emulated von Neumann Agent Architecture (RI-HEVNAA), is a novel approach to building a chatbot that mirrors the structure and functions of the human brain. It has three main SuperUnits (SUs): the Agent SuperUnit (A_SU), the Left Hemisphere SuperUnit (LH_SU), and the Right Hemisphere SuperUnit (RH_SU). Each of these SuperUnits has an Agent Central Processing Unit (A-CPU) inspired by the von Neumann architecture and a suite of Accelerators. The A-CPU has a Control Unit, a Memory Unit, and an Execution Unit.

1. The A_SU serves as the high-level manager of the chatbot system. It consists of five Accelerators:
    - Internal IO Accelerator
    - System Parameter Regulator Accelerator (SPR_A): Regulates low-complexity signals across the system.
    - State Control Accelerator (SC_A): Manages the overall system state.
    - LifeCycle Manager Accelerator (LM_A): Oversees life cycle events, like sleep schedules.
    - System Priority Regulator Accelerator (PR_A): Manages high-level system priorities.

2. The LH_SU corresponds to the left hemisphere of the human brain and handles tasks like speech and language processing. It includes three Accelerators:
    - Internal IO Accelerator
    - Linguistic Processing Accelerator (LP_A): Handles language and speech-related tasks.
    - Motor Coordination Accelerator (MC_A): Interfaces with the robot's physical movements.

3. The RH_SU corresponds to the right hemisphere and manages tasks like spatial and visual processing. It includes three Accelerators:
    - Internal IO Accelerator
    - Sensory Processing Accelerator (SP_A): Manages sensory inputs from the robot's environment.
    - Visual and Spatial Processing Accelerator (VSP_A): Handles spatial and visual-related tasks.

Communication between these SuperUnits occurs through the Internal IO Accelerator, which reads and writes data to the 'Agent Bus' and 'Interhemispheric Bus'. These busses are implemented as structured logs that can be read by various parts of the system. Access to the bus is controlled to prevent data collisions, using a system of lock requests and priority levels.

In addition to the Accelerators, a key part of the RI-HEVNAA architecture is the use of 'Pathways' and 'Tasks'. A Pathway is a JSON file opened by the A-CPU that outlines a sequence of Tasks to run. Each Task, a Python file, performs a specific operation. The output of one Task serves as the input to the next, forming a chain of operations. This design allows complex computations to be broken down into manageable, modular Tasks, promoting code reuse, and fostering a close resemblance to the organization and operation of the human brain.

The code implementation of this architecture is organized into different Python files for each Accelerator and set of Tasks, and uses JSON for structured data storage. The architecture is designed to be run on a Raspberry Pi with Ubuntu, utilizing six independent programs - one A-CPU and one set of Accelerators for each SuperUnit.

Overall, the RI-HEVNAA is a complex, sophisticated architecture for building a chatbot that blends principles from computer science and neuroscience, creating a system capable of emulating the diverse functionalities of the human brain in real-time.
