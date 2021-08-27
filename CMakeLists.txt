cmake_minimum_required(VERSION 2.8.3)

project(nav_dif)

find_package(catkin REQUIRED COMPONENTS
  rospy
  actionlib
  actionlib_msgs
  sensor_msgs
  geometry_msgs
  visualization_msgs
)

catkin_python_setup()

catkin_package(
  LIBRARIES ${PROJECT_NAME}
  CATKIN_DEPENDS rospy actionlib actionlib_msgs sensor_msgs geometry_msgs
)

catkin_install_python(
  PROGRAMS nodes/nav_dif
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

# Install launch files
install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)
