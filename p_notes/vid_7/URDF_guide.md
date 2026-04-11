# how to describe your robot/URDF file

- there are a lot of software components that all need to know the physcial characteristic of the robot.
- we store the information about the robot physical characteristic in `/robot_description` and this information is stored in the urdf (unified robot description format) format.

## link the joint
### step 1: Links

break the physical structure down to seperate components call links.

#### rule of choosing links:
- if two part can move indipendently of eachother, they have to be seperate links
- if it make sensse for the part to be serperated, make them seperate links. e.g. if a camera is attached to the end of a rod and the camera is moving with the rod, we still sepereate them because they are physcailly different and make sense they have different characteristic.

#### we get to choose where the origin of the link should be:
- it doesn't matter too much unless for rotating links which should have their origin at the <u>pivot point</u>

#### how r the links connected?
- each link except for the first one will have a parent link (other links it's connected to) and how it's connected to the parent. 
- each link can only have one parent, but can have many child link. 

### step 2: joints

- the connections between links are called joints
- joints defined the relationship between the origin between the coordinate frame of the links
- therefore, joints can determine the position and roatation of each links in space. 

#### joint type
- joint need to specify what type of motion it uses 
- four common type
    - revolute: rotational movement around a point with fixed start and stop angle aka fixed limits
        - robot arm
    - coninuous: rotational motion around a point with no fixed limits 
        - wheels
    - prismatic: linear translational motion 
        - linear actuator
    - fixed: child link doesn't move relative to the parent link

## the urdf syntax

### proper xml file:
#### start with a declaration:

`<?xml version="1.0"?>`

#### root tag

- then have a root tag, that every other tag live inside of. we can use this tag to name our robot which in this case is 'robot_1'.
- typically we put links tag and joints tag in there

```
<robot name='robot_1'>
    <link>
    </link>

    <joint>
    </joint>

    <link>
    </link>

    ...
</robot>
```

#### link tag

- each link tag have name
- also can specify three characteristic, they are <u>optional</u>
    - `<visual>`
        - this is what we normally see in rviz2 and gazebo
        - three optional aspect we can specify
            - `<geometry>`
                - box
                - cylinder
                - sphere
                - or we can specify path to a 3D mesh
            - `<origin>`
                - this is a offset for the geometry 
                - initially centered
            - `<material>`
                - color
                    - rgb triplet
                    - if we set up color earilier we can just set up the name of the material
                    - <u>this will only set color in rviz not gazebo</u>
        - <u> btw we can set multiple `<visual>` tag if we want to make more complex shape
    - `<collision>`
        - use for physic collision calculation 
        - optional property:
            - `<geometry>`
                - <u>this can be copy and pasted from `<visual>` tag</u>
                - best to simplify this at all time, like sometime we want complex mesh visually but collision we just want to make it a simple rectangle, for computational purposes.
            - `<origin>`
                - <u>this can be copy and pasted from `<visual>` tag</u>
        - <u> btw we can set multiple `<collision>` tag if we want to make more complex object
    - `<inertial>`
        - use in physic calculation
        - how the link respond to forces
        - optional property 
            - `<mass>` 
            - `<origin>` 
                - center of mass
                - this is the point the link can balance on
            - `<inertia>`
                - rotational inertia matrix 
                - describe how the distribution of mass affect rotation of the link
                - use wikipedia list of inertia matrixes to get a good approximation by generalizing our things into general shapes, to get matricies and tensors.


```
<link name="arm_link">
    <visual>
        <geometry>
            ...
        </geometry>

        <origin>
            ...
        </origin>

        <materials>
            ...
        </materials>
    </visual>

    <collision>
        <geometry>
            ...
        </geometry>

        <origin>
            ...
        </origin>
    </collision>

    <inertial> 
        <mass>
            ...
        </mass>

        <origin>
            ...
        </origin>

        <inertia>
            ...
        </inertia>
    </inertial>

    ...
</link>
```