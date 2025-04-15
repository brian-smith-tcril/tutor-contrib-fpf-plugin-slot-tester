from tutormfe.hooks import PLUGIN_SLOTS

PLUGIN_SLOTS.add_items([
    (
        "learner-dashboard",
        "course_list_slot",
        """
        {
          op: PLUGIN_OPERATIONS.Insert,
          widget: {
            id: 'custom_course_list',
            type: DIRECT_PLUGIN,
            RenderWidget: () => (
              <h1 style={{textAlign: 'center'}}>😀</h1>
            ),
          },
        }"""
    ),
    (
        "learner-dashboard",
        "course_list_slot_alias",
        """
        {
          op: PLUGIN_OPERATIONS.Insert,
          widget: {
            id: 'custom_course_list',
            type: DIRECT_PLUGIN,
            RenderWidget: () => (
              <h1 style={{textAlign: 'center'}}>🥸</h1>
            ),
          },
        }"""
    )
])
