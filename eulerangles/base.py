from dataclasses import dataclass


@dataclass
class ConversionMeta:
    """
    A simple object holding metadata explaining how to interpret Euler angles in the context of
    density reconstruction from transmission electron microscopy data.

    software: str
        the name of the software package
    axes: str
        a valid non-sequential sequence of axes e.g. 'zxz', 'yxz'
    intrinsic: bool
        True - the euler angles represent intrinsic rotations, the coordinate system moves with
        the rotating rigid body
        False - the euler angles represent extrinsic rotations, the rigid body rotates with
        respect to a fixed coordinate system
    right_handed_rotation: bool
        True - the euler angles represent right hand rotations in a right handed coordinate system
        False - the euler angles represent left hand rotations in a right handed coordinate system
    active_transformation: bool
        True - the transformation is an active transformation
        False - the transformation is a passive transformation
        this property is compared between ConversionMeta objects when deciding whether
        or not to invert rotation matrices derived from euler angles during conversion
    """
    software: str
    axes: str
    intrinsic: bool
    right_handed_rotation: bool
    active_transformation: bool


