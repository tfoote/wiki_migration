## Running

\`nav_graph_builder.launch\` launches the navigation graph builder,
which generates the occupancy grids and roadmap given the output from
the graph slam system in the [graph_slam](graph_slam) package.

\`move_base_topo.launch\` launches the navigation system, that takes in
goals and uses the navigation graph to do hybrid metric-topological
planning, and send the resulting waypoints to move_base.
