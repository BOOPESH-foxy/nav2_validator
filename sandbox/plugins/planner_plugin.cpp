#include "rclcpp/rclcpp.hpp"

class PlannerPlugin : public rclcpp::Node {
public:
    PlannerPlugin() : Node("planner_plugin") {
        declare_parameter<double>("speed", 1.0);
        declare_parameter<double>("tolerance", 0.1);
        declare_parameter<int>("max_iterations", 100);
    }
};
