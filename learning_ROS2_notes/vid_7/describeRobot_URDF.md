# How to describe robot? URDF

## steps to describing a robot:

1. break physical stucture down to seperate components called links (links are different components)
    1. if two links can move independently from eachother
    2. seperate physical component: sensor and structural component
    3. something that can be removed
2. choose the origin of the coordinate system links
    1. doesn't matter too much except for rotating links
    2. rotating links: have the origin at the pivot point 
3. decide how links relate to eachother with joints (joints connects two or more links together)
    1. more sepecifically, joints defines the relationship between two coordinate system of seperate links
    2. each links apart the first one, have:
        1. what other links it's connected to
        2. it's parents
        3. how it's connected to parent
        4. one link can only have one parent
        5. one link can have multiple childs
    3. decide what the joint type is:
        1. revolute
            1. rotation abt a point
            2. fixed start and stop angle, aka fixed limits
        2. continuous
            1. rotation abt a point
            2. no fixed limits, aka spin freely forever
        3. prismatic
            1. linear translational motion
        4. fixed
            1. child link doesn't move relative to the parent link

## the URDF syntax

URDF use xml file type with a series of tag

### xml doc start with xml declaration

``` 
<?xml version="1.0"?>
```

### then root tag, which is the robot tag

attribute: name

live in side the root tag: link / joint
``` 
<?xml version="1.0"?>
<robot name="robot">
    <link>
    </linkt>

    <joint>
    </joint>

    <link>
    </link>

    ...
</robot>
```

### link tag

attribute: name

characteristic: visual collision inertial - (all is optional)

- visual
    - what we see in rviz and gazebo
    - geometry
        - general shape 
            - can even specify a path to a 3d mesh
    - origin
        - offset of the geometry, so it don't have to be centered all the time
    - material
        - colour 
        - you can set up a material, and reference to it 
    - multiple visual tag to make complexed shape
- collision
    - use for physical calculation
    - geometry 
        - can be copy and pasted from visual tagh, or use simplier shape for easier computation
    - origin 
        - can be copy and pasted from visual tag
- inertial
    - use for physic calculation for forces 
    - mass
    - origin
        - center of mass
    - inertia 
        - rotational inertia matrix 
        - describe how distribution of mass effect rotation
        - wiki have a lot of approx for rotational inertia matrix

``` 
<?xml version="1.0"?>
<robot name="robot">
    <link namw="arm_link">
        <visual>
            <geometry>
            <origin>
            <material>
        </visual>
        <collision>
            <geometry>
            <origin>
        </collision>
        <inertial>
            <mass>
            <origin>
            <inertia>
        </inertial>
    </link>

    <joint>
    </joint>

    <link>
    </link>

    ...
</robot>
```

### joint tag

attribute: name type

characteristic: parent child origin - (all is optional)

- joint type is:
    1. revolute
        1. rotation abt a point
        2. fixed start and stop angle, aka fixed limits
    2. continuous
        1. rotation abt a point
        2. no fixed limits, aka spin freely forever
    3. prismatic
        1. linear translational motion
    4. fixed
        1. child link doesn't move relative to the parent link
- origin
    - relationship of the joint before any motion is applied
- for non-fixed joint, we need to specify extra characteristic
    - axis
        - which axis the joint moves along or around
    - limit
        - determine physical limit of joint t5y6
        - upper and lower positional limit
            - rad or meter
        - velocity limit
            - rad/s or m/s
        - effort limit
            - N or N/m

``` 
<?xml version="1.0"?>
<robot name="robot" type="revolute>
    <link>
    </link>

    <joint>
        <parent link="slider_link" />
        <child link="arm_link" />
        <origin xyz="0.25 0 0.15" rpy="0 0 0" />

        <axis xyz="0 -1 0" />
        <limit lower="0" upper="${pi/2}" velocity="100" effort="100" />
    </joint>

    <link>
    </link>

    ...
</robot>
```