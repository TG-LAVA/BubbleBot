cmake_minimum_required(VERSION 3.8)
project(base_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(action_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()


rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/JointAngles.msg"
  "msg/ServoStatus.msg"
  "srv/SendAngles.srv"
  "srv/OrderRequest.srv"
  "srv/BaseDBCommand.srv"
  "srv/BaseCommand.srv"
  "srv/WorkFlow.srv"
  # "srv/MyService.srv"
  # "action/MyAction.action"
  # "msg/MyMessage.msg"
  DEPENDENCIES builtin_interfaces action_msgs geometry_msgs std_msgs
)

ament_export_dependencies(geometry_msgs)
ament_package()
