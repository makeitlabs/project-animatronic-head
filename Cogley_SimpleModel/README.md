# Cogley Simple Model

Cogley_SimpleModel.btngo: Bottango file

Cogley_SimpleModel.fbx: Fusion 360 export

This file is large and will be added only via release:

Cogley_SimpleModel.f3z: Fusion 360 source


## Fusion to Bottango:

In Fusion, create your model.

You will want to convert various parts to components, and ensure their hierarchy makes sense (e.g. if building a robot arm, the base should be top level, then the first arm section, then the next arm section, all the way out).

Also create a separate design with nothing in it, and call it "joint" or something similar.

Insert the "joint" into the design wherever you want a joint.

Now, you need to update the hierarchy that the joint appears at the right position in the tree. You'll need to break the link to the joint file, and then you can move components under/into the joint.

Repeat for all joints.

It probably wouldn't hurt to make sure things are named with reasonable name (your future self will thank you).

Export as FBX (this is under the File menu for the whole design).  FBX conversion takes place in the cloud, and may take a minute or so.

Import into Bottango.

There will be a bunch of extra nodes in the hierarchy tree.  Go ahead and collapse ones that make sense, and convert your empty joint objects to joints.  (really, there's a lot of extra junk in the tree, it might take a little trial and error until you get the hang of which items to collapse, which to convert to joints, etc.).

Hopefully it all works.
