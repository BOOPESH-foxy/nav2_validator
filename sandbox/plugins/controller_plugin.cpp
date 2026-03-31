#include "rclcpp/rclcpp.hpp"

class ControllerPlugin : public rclcpp::Node {
public:
    ControllerPlugin() : Node("controller_plugin") {
        declare_parameter<double>("kp", 1.0);
        declare_parameter<double>("kd", 0.01);
        declare_parameter<double>("max_vel", 2.0);
        declare_parameter<double>("min_vel", 0.1);
    }
};
