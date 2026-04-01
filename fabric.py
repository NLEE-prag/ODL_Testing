import os
from fabric_cicd import FabricWorkspace, publish_all_items, unpublish_all_orphan_items
 
# Initialize the FabricWorkspace object with the required parameters
target_workspace = FabricWorkspace(
    workspace_id = "c20c4816-fbe6-46ec-abfd-c0de73c957c4",
    environment = "prod",
    repository_directory = os.path.dirname(__file__),
    item_type_in_scope = None,
)
 
# Publish all items defined in item_type_in_scope
publish_all_items(target_workspace)
 
# Unpublish all items defined in item_type_in_scope not found in repository
unpublish_all_orphan_items(target_workspace)
