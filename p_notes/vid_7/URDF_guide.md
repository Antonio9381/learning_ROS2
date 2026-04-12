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

### urdf file structure:
#### start with a declaration:

a proper xml file start with `<?xml version="1.0"?>`

#### root tag

- then have a root tag, that every other tag live inside of. we can use this tag to name our robot which in this case is 'robot_1'.
- typically we put links tag and joints tag in there
    - there are other tag, and you can make your own tag
    - you make determine what tag to include by seeing what tag is required in different nodes 
    - common tag
        - material tag: name a color so we can use it multiple times
        - gazebo tag: doing simulation we can specify different parameter for how we want the simulation to work
        - transmission tag: define how actuator is connected to a joint

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
        - <u> btw we can set multiple `<visual>` tag if we want to make more complex shape</u>
    - `<collision>`
        - use for physic collision calculation 
        - optional property:
            - `<geometry>`
                - <u>this can be copy and pasted from `<visual>` tag</u>
                - best to simplify this at all time, like sometime we want complex mesh visually but collision we just want to make it a simple rectangle, for computational purposes.
            - `<origin>`
                - <u>this can be copy and pasted from `<visual>` tag</u>
        - <u> btw we can set multiple `<collision>` tag if we want to make more complex object</u>
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

#### joint tag

- each joint needs the following specified
    - for both fixed and non-fixed joints:
        - name
        - type
        - parent and child link
        - origin
            - rpy is roll pitch and yaw
    - for non-fixed joints:
        - axis
            - axis of rotation for recolute and continuous joints
            - axis of translation for prismatic joints
        - limit
            - determines the physical limitation
            - upper and lower
                - position limit in rad or meter
            - velocity 
                - speed limit in rad/s or m/s
            - effort
                - in newton or newton/meter

```
<joint name="arm_joint" type="revolute>
    <parent link="slider_link" />
    <child link="arm_link" />
    <origin xyz="0.25 0 0.15" rpy="0 0 0" />

    <axis xyz="0 -1 0" />
    <limit lower="0" upper="${pi/2}" velocity="100" effort="100" />
</joint>
```

### naming convention for urdf files 
- "_link" on every link you named
- "_joint" on every joint you named

### ros's xacro tool
xacro is short for xml macro

#### it's a tool that let us take urdf file can do a lot of things such as:
- use xacro to split file into multiple files
- avoid repeating ourselves

#### to enable xacro to our file, all we need is to add
```
<robot xmlns:xacro="http://www.ros.org/wiki/xacro">
```

### how we using xacro
- we make a lot of split up urdf files
- xacro combined them and process it into 1 urdf file
- xacro publish to `robot_state_publisher`
- `robot_state_publisher` publish the single processed urdf file to `/robot_description`

### ultiple urdf files structure with xacro:
- we can have a main file that's called "my_robot.urdf.xacro"
    - use this file to include other files
```
<?xml version="1.0"?>

<robot name='robot_1' xmlns:xacro="http://www.ros.org/wiki/xacro">
    
    <xacro:include filename="my_materials.xacro" />

    <link> ... </link>

    <joint> ... </joint>

    <link> ... </link>
</robot>
```
- e.g. "my_materials.xacro"
    - <u>notice we don't have to include name bc this just copy and paste into the position of the main file</u>
        - we can give it a name so that it will be treated as a robot on it's own but it depends on situation
    - rgba is red green blue alpha
```
<?xml version="1.0"?>

<robot xmlns:xacro="http://www.ros.org/wiki/xacro">
    <material name="white">
        <color rgba="1 1 1 1" />
    </material>
</robot>
```

### xacro simplification that can help us make less mistake
- property: like a variable in coding
    - `<xacro:property name="arm_radius" value="0.5" />`
- mathematical operators: perform operation and use mathematical constant
    - `<cylinder length="${4*arm_radius + pi}">`
- macros:
    - basically like a template for tag that we can input in
    - like a function that format tags
        - template
```
<xacro:macro name="inertial_box" param="mass x y z *origin">
    <inertial>
        <xacro:insert_block name="origin" />
        <mass value="${mass}" />
        <inertia ixx="${(1/2) * mass * (y*y+z*z)}" />
    </inertial>
</xacro:macro>
```
- how to use later
```
<xacro:inertial_box mass="12" x="2" y="3" z="4">
    <origin xyz="0 2 4" rpy="0 0 0" />
</xacro:inertial_box>
```
- will expand to:
```
<inertial>
    <origin xyz="0 2 4" rpy="0 0 0" />
    <mass value="12" />
    <inertia ixx="25" />
</inertial>
```

## final urdf code
```
<?xml version="1.0"?>

<robot name='robot_1' xmlns:xacro="http://www.ros.org/wiki/xacro">
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
    </link>

    <joint name="arm_joint" type="revolute>
        <parent link="slider_link" />
        <child link="arm_link" />
        <origin xyz="0.25 0 0.15" rpy="0 0 0" />

        <axis xyz="0 -1 0" />
        <limit lower="0" upper="${pi/2}" velocity="100" effort="100" />
    </joint>

    <link>
    </link>

    <joint>
    </joint>

    ...
</robot>
```