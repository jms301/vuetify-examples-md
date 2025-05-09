# Vuetify component v-list - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <div>
      <v-list v-bind="props">
        <v-list-item
          v-for="n in 3"
          :key="n"
          :prepend-avatar="avatar ? 'https://randomuser.me/api/portraits/women/8.jpg' : undefined"
          :title="'Item ' + n"
          subtitle="Lorem ipsum dolor sit amet consectetur adipisicing elit"
        ></v-list-item>
      </v-list>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="avatar" label="Show avatars"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-list'
  const model = ref('default')
  const options = ['two-lines', 'three-lines']
  const avatar = ref(false)

  const lines = computed(() => {
    return {
      default: 'one',
      'two-lines': 'two',
      'three-lines': 'three',
    }[model.value]
  })

  const props = computed(() => {
    return {
      lines: lines.value,
    }
  })
  const itemProps = computed(() => {
    return {
      'v-for': 'n in 3',
      ':key': 'n',
      ':title': `'Item ' + n`,
      subtitle: 'Lorem ipsum dolor sit amet consectetur adipisicing elit',
      ':prepend-avatar': avatar.value ? 'https://randomuser.me/api/portraits/women/8.jpg' : undefined,
    }
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>
  <v-list-item${propsToString(itemProps.value, 2)}></v-list-item>
</${name}>`
  })
</script>

```

# Vuetify component v-list - prop variant

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="300"
  >
    <v-list>
      <v-list-subheader>Plain Variant</v-list-subheader>

      <v-list-item
        v-for="(item, i) in items"
        :key="i"
        :value="item"
        color="primary"
        variant="plain"
      >
        <template v-slot:prepend>
          <v-icon :icon="item.icon"></v-icon>
        </template>

        <v-list-item-title v-text="item.text"></v-list-item-title>
      </v-list-item>
    </v-list>

    <v-list>
      <v-list-subheader>Tonal Variant</v-list-subheader>

      <v-list-item
        v-for="(item, i) in items"
        :key="i"
        :value="item"
        color="primary"
        variant="tonal"
      >
        <template v-slot:prepend>
          <v-icon :icon="item.icon"></v-icon>
        </template>

        <v-list-item-title v-text="item.text"></v-list-item-title>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup>
  const items = [
    { text: 'Real-Time', icon: 'mdi-clock' },
    { text: 'Audience', icon: 'mdi-account' },
    { text: 'Conversions', icon: 'mdi-flag' },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        { text: 'Real-Time', icon: 'mdi-clock' },
        { text: 'Audience', icon: 'mdi-account' },
        { text: 'Conversions', icon: 'mdi-flag' },
      ],
    }),
  }
</script>

```

# Vuetify component v-list - prop items

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="300"
  >
    <v-list :items="items"></v-list>
  </v-card>
</template>

<script setup>
  const items = [
    {
      title: 'Item #1',
      value: 1,
    },
    {
      title: 'Item #2',
      value: 2,
    },
    {
      title: 'Item #3',
      value: 3,
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          title: 'Item #1',
          value: 1,
        },
        {
          title: 'Item #2',
          value: 2,
        },
        {
          title: 'Item #3',
          value: 3,
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-list - prop rounded

Example code

```vue
<template>
  <v-card
    class="mx-auto pa-2"
    max-width="300"
  >
    <v-list>
      <v-list-subheader>REPORTS</v-list-subheader>

      <v-list-item
        v-for="(item, i) in items"
        :key="i"
        :value="item"
        color="primary"
        rounded="xl"
      >
        <template v-slot:prepend>
          <v-icon :icon="item.icon"></v-icon>
        </template>

        <v-list-item-title v-text="item.text"></v-list-item-title>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup>
  const items = [
    { text: 'Real-Time', icon: 'mdi-clock' },
    { text: 'Audience', icon: 'mdi-account' },
    { text: 'Conversions', icon: 'mdi-flag' },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        { text: 'Real-Time', icon: 'mdi-clock' },
        { text: 'Audience', icon: 'mdi-account' },
        { text: 'Conversions', icon: 'mdi-flag' },
      ],
    }),
  }
</script>

```

# Vuetify component v-list - misc card list

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="375"
  >
    <v-img
      class="text-white"
      height="300px"
      src="https://cdn.vuetifyjs.com/images/lists/ali.png"
      cover
    >
      <div class="d-flex flex-column h-100">
        <v-card-title class="d-flex ga-2 px-2">
          <v-btn icon="mdi-chevron-left" variant="text"></v-btn>
          <v-spacer></v-spacer>
          <v-btn icon="mdi-pencil" variant="text"></v-btn>
          <v-btn icon="mdi-dots-vertical" variant="text"></v-btn>
        </v-card-title>

        <v-spacer></v-spacer>

        <v-card-title class="pb-6 text-center">
          <div class="text-h4">Ali Conners</div>
        </v-card-title>
      </div>
    </v-img>

    <v-list lines="two">
      <v-list-item>
        <template v-slot:prepend>
          <v-avatar>
            <v-icon color="indigo" icon="mdi-phone"></v-icon>
          </v-avatar>
        </template>

        <v-list-item-title>(650) 555-1234</v-list-item-title>
        <v-list-item-subtitle>Mobile</v-list-item-subtitle>

        <template v-slot:append>
          <v-avatar>
            <v-icon icon="mdi-message-text"></v-icon>
          </v-avatar>
        </template>
      </v-list-item>

      <v-list-item>
        <template v-slot:prepend>
          <v-avatar></v-avatar>
        </template>

        <v-list-item-title>(323) 555-6789</v-list-item-title>
        <v-list-item-subtitle>Work</v-list-item-subtitle>

        <template v-slot:append>
          <v-avatar>
            <v-icon icon="mdi-message-text"></v-icon>
          </v-avatar>
        </template>
      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-item>
        <template v-slot:prepend>
          <v-avatar>
            <v-icon color="indigo" icon="mdi-email"></v-icon>
          </v-avatar>
        </template>

        <v-list-item-title>aliconnors@example.com</v-list-item-title>
        <v-list-item-subtitle>Personal</v-list-item-subtitle>
      </v-list-item>

      <v-list-item>
        <template v-slot:prepend>
          <v-avatar></v-avatar>
        </template>

        <v-list-item-title>ali_connors@example.com</v-list-item-title>
        <v-list-item-subtitle>Work</v-list-item-subtitle>
      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-item>
        <template v-slot:prepend>
          <v-avatar>
            <v-icon color="indigo" icon="mdi-map-marker"></v-icon>
          </v-avatar>
        </template>

        <v-list-item-title>1400 Main Street</v-list-item-title>
        <v-list-item-subtitle>Orlando, FL 79938</v-list-item-subtitle>
      </v-list-item>
    </v-list>
  </v-card>
</template>

```

# Vuetify component v-list - prop density

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="300"
  >
    <v-list density="compact">
      <v-list-subheader>REPORTS</v-list-subheader>

      <v-list-item
        v-for="(item, i) in items"
        :key="i"
        :value="item"
        color="primary"
      >
        <template v-slot:prepend>
          <v-icon :icon="item.icon"></v-icon>
        </template>

        <v-list-item-title v-text="item.text"></v-list-item-title>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup>
  const items = [
    { text: 'Real-Time', icon: 'mdi-clock' },
    { text: 'Audience', icon: 'mdi-account' },
    { text: 'Conversions', icon: 'mdi-flag' },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        { text: 'Real-Time', icon: 'mdi-clock' },
        { text: 'Audience', icon: 'mdi-account' },
        { text: 'Conversions', icon: 'mdi-flag' },
      ],
    }),
  }
</script>

```

# Vuetify component v-list - slot expansion lists

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="500"
  >
    <v-toolbar
      color="teal"
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Topics</v-toolbar-title>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-toolbar>

    <v-list>
      <v-list-group
        v-for="item in items"
        :key="item.title"
        v-model="item.active"
        :prepend-icon="item.action"
      >
        <template v-slot:activator>
          <v-list-item-header>
            <v-list-item-title v-text="item.title"></v-list-item-title>
          </v-list-item-header>
        </template>

        <v-list-item
          v-for="child in item.items"
          :key="child.title"
        >
          <v-list-item-header>
            <v-list-item-title v-text="child.title"></v-list-item-title>
          </v-list-item-header>
        </v-list-item>
      </v-list-group>
    </v-list>
  </v-card>
</template>

<script setup>
  const items = [
    {
      action: 'mdi-ticket',
      items: [{ title: 'List Item' }],
      title: 'Attractions',
    },
    {
      action: 'mdi-silverware-fork-knife',
      active: true,
      items: [
        { title: 'Breakfast & brunch' },
        { title: 'New American' },
        { title: 'Sushi' },
      ],
      title: 'Dining',
    },
    {
      action: 'mdi-school',
      items: [{ title: 'List Item' }],
      title: 'Education',
    },
    {
      action: 'mdi-human-male-female-child',
      items: [{ title: 'List Item' }],
      title: 'Family',
    },
    {
      action: 'mdi-bottle-tonic-plus',
      items: [{ title: 'List Item' }],
      title: 'Health',
    },
    {
      action: 'mdi-briefcase',
      items: [{ title: 'List Item' }],
      title: 'Office',
    },
    {
      action: 'mdi-tag',
      items: [{ title: 'List Item' }],
      title: 'Promotions',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          action: 'mdi-ticket',
          items: [{ title: 'List Item' }],
          title: 'Attractions',
        },
        {
          action: 'mdi-silverware-fork-knife',
          active: true,
          items: [
            { title: 'Breakfast & brunch' },
            { title: 'New American' },
            { title: 'Sushi' },
          ],
          title: 'Dining',
        },
        {
          action: 'mdi-school',
          items: [{ title: 'List Item' }],
          title: 'Education',
        },
        {
          action: 'mdi-human-male-female-child',
          items: [{ title: 'List Item' }],
          title: 'Family',
        },
        {
          action: 'mdi-bottle-tonic-plus',
          items: [{ title: 'List Item' }],
          title: 'Health',
        },
        {
          action: 'mdi-briefcase',
          items: [{ title: 'List Item' }],
          title: 'Office',
        },
        {
          action: 'mdi-tag',
          items: [{ title: 'List Item' }],
          title: 'Promotions',
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-list - misc actions

Example code

```vue
<template>
  <v-card class="mx-auto" max-width="400">
    <v-toolbar color="purple">
      <v-btn icon="mdi-menu"></v-btn>
      <v-toolbar-title>Settings</v-toolbar-title>
      <v-btn icon="mdi-magnify"></v-btn>
    </v-toolbar>

    <v-list lines="three">
      <v-list-subheader>User Controls</v-list-subheader>
      <v-list-item
        v-for="item in userControls"
        :key="item.value"
        :subtitle="item.subtitle"
        :title="item.title"
      ></v-list-item>
    </v-list>

    <v-divider></v-divider>

    <v-list
      v-model:selected="settingsSelection"
      lines="three"
      select-strategy="leaf"
    >
      <v-list-subheader>General</v-list-subheader>
      <v-list-item
        v-for="item in settingsItems"
        :key="item.value"
        :subtitle="item.subtitle"
        :title="item.title"
        :value="item.value"
      >
        <template v-slot:prepend="{ isSelected, select }">
          <v-list-item-action start>
            <v-checkbox-btn :model-value="isSelected" @update:model-value="select"></v-checkbox-btn>
          </v-list-item-action>
        </template>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const userControls = [
    { title: 'Content filtering', subtitle: 'Set the content filtering level to restrict appts that can be downloaded' },
    { title: 'Password', subtitle: 'Require password for purchase or use password to restrict purchase' },
  ]

  const settingsItems = [
    { value: 'notifications', title: 'Notifications', subtitle: 'Notify me about updates to apps or games that I downloaded' },
    { value: 'sound', title: 'Sound', subtitle: 'Auto-update apps at any time. Data charges may apply' },
    { value: 'widgets', title: 'Auto-add widgets', subtitle: 'Automatically add home screen widgets when downloads complete' },
  ]

  const settingsSelection = ref([])
</script>

<script>
  export default {
    data: () => ({
      userControls: [
        { title: 'Content filtering', subtitle: 'Set the content filtering level to restrict appts that can be downloaded' },
        { title: 'Password', subtitle: 'Require password for purchase or use password to restrict purchase' },
      ],

      settingsItems: [
        { value: 'notifications', title: 'Notifications', subtitle: 'Notify me about updates to apps or games that I downloaded' },
        { value: 'sound', title: 'Sound', subtitle: 'Auto-update apps at any time. Data charges may apply' },
        { value: 'widgets', title: 'Auto-add widgets', subtitle: 'Automatically add home screen widgets when downloads complete' },
      ],

      settingsSelection: [],
    }),
  }
</script>

```

# Vuetify component v-list - prop nav

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    width="256"
  >
    <v-layout>
      <v-navigation-drawer absolute permanent>
        <v-list>
          <v-list-item
            prepend-avatar="https://cdn.vuetifyjs.com/images/john.png"
            subtitle="john@google.com"
            title="John Leider"
          >
            <template v-slot:append>
              <v-btn
                icon="mdi-menu-down"
                size="small"
                variant="text"
              ></v-btn>
            </template>
          </v-list-item>
        </v-list>

        <v-divider></v-divider>

        <v-list
          :lines="false"
          density="compact"
          nav
        >
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            :value="item"
            color="primary"
          >
            <template v-slot:prepend>
              <v-icon :icon="item.icon"></v-icon>
            </template>

            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>

      <v-main style="height: 354px;"></v-main>
    </v-layout>
  </v-card>
</template>

<script setup>
  const items = [
    { text: 'My Files', icon: 'mdi-folder' },
    { text: 'Shared with me', icon: 'mdi-account-multiple' },
    { text: 'Starred', icon: 'mdi-star' },
    { text: 'Recent', icon: 'mdi-history' },
    { text: 'Offline', icon: 'mdi-check-circle' },
    { text: 'Uploads', icon: 'mdi-upload' },
    { text: 'Backups', icon: 'mdi-cloud-upload' },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        { text: 'My Files', icon: 'mdi-folder' },
        { text: 'Shared with me', icon: 'mdi-account-multiple' },
        { text: 'Starred', icon: 'mdi-star' },
        { text: 'Recent', icon: 'mdi-history' },
        { text: 'Offline', icon: 'mdi-check-circle' },
        { text: 'Uploads', icon: 'mdi-upload' },
        { text: 'Backups', icon: 'mdi-cloud-upload' },
      ],
    }),
  }
</script>

```

# Vuetify component v-list - misc single line list

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="500"
  >
    <v-toolbar color="deep-purple-accent-4">
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>New Chat</v-toolbar-title>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
    </v-toolbar>

    <v-list>
      <v-list-subheader>Recent chat</v-list-subheader>

      <v-list-item
        v-for="chat in recent"
        :key="chat.title"
      >
        <template v-slot:prepend>
          <v-avatar>
            <v-img :src="chat.avatar"></v-img>
          </v-avatar>
        </template>

        <v-list-item-title>{{ chat.title }}</v-list-item-title>

        <template v-slot:append>
          <v-avatar>
            <v-icon :color="chat.active ? 'deep-purple accent-4' : 'grey'">
              mdi-message-outline
            </v-icon>
          </v-avatar>
        </template>
      </v-list-item>
    </v-list>

    <v-divider></v-divider>

    <v-list>
      <v-list-subheader>Previous chats</v-list-subheader>

      <v-list-item
        v-for="chat in previous"
        :key="chat.title"
      >
        <template v-slot:prepend>
          <v-avatar>
            <v-img :src="chat.avatar"></v-img>
          </v-avatar>
        </template>

        <v-list-item-title v-text="chat.title"></v-list-item-title>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup>
  const recent = [
    {
      active: true,
      avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
      title: 'Jason Oner',
    },
    {
      active: true,
      avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
      title: 'Mike Carlson',
    },
    {
      avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
      title: 'Cindy Baker',
    },
    {
      avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
      title: 'Ali Connors',
    },
  ]
  const previous = [{
    title: 'Travis Howard',
    avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
  }]
</script>

<script>
  export default {
    data: () => ({
      recent: [
        {
          active: true,
          avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
          title: 'Jason Oner',
        },
        {
          active: true,
          avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
          title: 'Mike Carlson',
        },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
          title: 'Cindy Baker',
        },
        {
          avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
          title: 'Ali Connors',
        },
      ],
      previous: [{
        title: 'Travis Howard',
        avatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
      }],
    }),
  }
</script>

```

# Vuetify component v-list - prop disabled

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="300"
  >
    <v-list disabled>
      <v-list-subheader>REPORTS</v-list-subheader>

      <v-list-item
        v-for="(item, i) in items"
        :key="i"
      >
        <template v-slot:prepend>
          <v-icon :icon="item.icon"></v-icon>
        </template>

        <v-list-item-title v-text="item.text"></v-list-item-title>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup>
  const items = [
    { text: 'Real-Time', icon: 'mdi-clock' },
    { text: 'Audience', icon: 'mdi-account' },
    { text: 'Conversions', icon: 'mdi-flag' },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        { text: 'Real-Time', icon: 'mdi-clock' },
        { text: 'Audience', icon: 'mdi-account' },
        { text: 'Conversions', icon: 'mdi-flag' },
      ],
    }),
  }
</script>

```

# Vuetify component v-list - prop shaped

Example code

```vue
<template>
  <v-card
    class="mx-auto pa-2"
    max-width="300"
  >
    <v-list>
      <v-list-subheader>REPORTS</v-list-subheader>

      <v-list-item
        v-for="(item, i) in items"
        :key="i"
        :value="item"
        color="primary"
        rounded="shaped"
      >
        <template v-slot:prepend>
          <v-icon :icon="item.icon"></v-icon>
        </template>

        <v-list-item-title v-text="item.text"></v-list-item-title>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup>
  const items = [
    { text: 'Real-Time', icon: 'mdi-clock' },
    { text: 'Audience', icon: 'mdi-account' },
    { text: 'Conversions', icon: 'mdi-flag' },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        { text: 'Real-Time', icon: 'mdi-clock' },
        { text: 'Audience', icon: 'mdi-account' },
        { text: 'Conversions', icon: 'mdi-flag' },
      ],
    }),
  }
</script>

```

# Vuetify component v-list - prop sub group

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    width="300"
  >
    <v-list v-model:opened="open">
      <v-list-item prepend-icon="mdi-home" title="Home"></v-list-item>

      <v-list-group value="Users">
        <template v-slot:activator="{ props }">
          <v-list-item
            v-bind="props"
            prepend-icon="mdi-account-circle"
            title="Users"
          ></v-list-item>
        </template>

        <v-list-group value="Admin">
          <template v-slot:activator="{ props }">
            <v-list-item
              v-bind="props"
              title="Admin"
            ></v-list-item>
          </template>

          <v-list-item
            v-for="([title, icon], i) in admins"
            :key="i"
            :prepend-icon="icon"
            :title="title"
            :value="title"
          ></v-list-item>
        </v-list-group>

        <v-list-group value="Actions">
          <template v-slot:activator="{ props }">
            <v-list-item
              v-bind="props"
              title="Actions"
            ></v-list-item>
          </template>

          <v-list-item
            v-for="([title, icon], i) in cruds"
            :key="i"
            :prepend-icon="icon"
            :title="title"
            :value="title"
          ></v-list-item>
        </v-list-group>
      </v-list-group>
    </v-list>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const open = ref(['Users'])

  const admins = [
    ['Management', 'mdi-account-multiple-outline'],
    ['Settings', 'mdi-cog-outline'],
  ]
  const cruds = [
    ['Create', 'mdi-plus-outline'],
    ['Read', 'mdi-file-outline'],
    ['Update', 'mdi-update'],
    ['Delete', 'mdi-delete'],
  ]
</script>

<script>
  export default {
    data: () => ({
      open: ['Users'],
      admins: [
        ['Management', 'mdi-account-multiple-outline'],
        ['Settings', 'mdi-cog-outline'],
      ],
      cruds: [
        ['Create', 'mdi-plus-outline'],
        ['Read', 'mdi-file-outline'],
        ['Update', 'mdi-update'],
        ['Delete', 'mdi-delete'],
      ],
    }),
  }
</script>

```

# Vuetify component v-list - prop items custom

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="300"
  >
    <v-list
      :items="items"
      item-title="name"
      item-value="id"
    ></v-list>
  </v-card>
</template>

<script setup>
  const items = [
    {
      name: 'Item #1',
      id: 1,
    },
    {
      name: 'Item #2',
      id: 2,
    },
    {
      name: 'Item #3',
      id: 3,
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          name: 'Item #1',
          id: 1,
        },
        {
          name: 'Item #2',
          id: 2,
        },
        {
          name: 'Item #3',
          id: 3,
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-list - prop two line and subheader

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="600"
  >
    <v-toolbar color="secondary">
      <v-btn icon="mdi-menu" variant="text"></v-btn>

      <v-toolbar-title>My files</v-toolbar-title>

      <v-btn icon="mdi-magnify" variant="text"></v-btn>

      <v-btn icon="mdi-view-module" variant="text"></v-btn>
    </v-toolbar>

    <v-list lines="two">
      <v-list-subheader inset>Folders</v-list-subheader>

      <v-list-item
        v-for="folder in folders"
        :key="folder.title"
        :subtitle="folder.subtitle"
        :title="folder.title"
      >
        <template v-slot:prepend>
          <v-avatar color="grey-lighten-1">
            <v-icon color="white">mdi-folder</v-icon>
          </v-avatar>
        </template>

        <template v-slot:append>
          <v-btn
            color="grey-lighten-1"
            icon="mdi-information"
            variant="text"
          ></v-btn>
        </template>
      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-subheader inset>Files</v-list-subheader>

      <v-list-item
        v-for="file in files"
        :key="file.title"
        :subtitle="file.subtitle"
        :title="file.title"
      >
        <template v-slot:prepend>
          <v-avatar :color="file.color">
            <v-icon color="white">{{ file.icon }}</v-icon>
          </v-avatar>
        </template>

        <template v-slot:append>
          <v-btn
            color="grey-lighten-1"
            icon="mdi-information"
            variant="text"
          ></v-btn>
        </template>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup>
  const files = [
    {
      color: 'blue',
      icon: 'mdi-clipboard-text',
      subtitle: 'Jan 20, 2014',
      title: 'Vacation itinerary',
    },
    {
      color: 'amber',
      icon: 'mdi-gesture-tap-button',
      subtitle: 'Jan 10, 2014',
      title: 'Kitchen remodel',
    },
  ]
  const folders = [
    {
      subtitle: 'Jan 9, 2014',
      title: 'Photos',
    },
    {
      subtitle: 'Jan 17, 2014',
      title: 'Recipes',
    },
    {
      subtitle: 'Jan 28, 2014',
      title: 'Work',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      files: [
        {
          color: 'blue',
          icon: 'mdi-clipboard-text',
          subtitle: 'Jan 20, 2014',
          title: 'Vacation itinerary',
        },
        {
          color: 'amber',
          icon: 'mdi-gesture-tap-button',
          subtitle: 'Jan 10, 2014',
          title: 'Kitchen remodel',
        },
      ],
      folders: [
        {
          subtitle: 'Jan 9, 2014',
          title: 'Photos',
        },
        {
          subtitle: 'Jan 17, 2014',
          title: 'Recipes',
        },
        {
          subtitle: 'Jan 28, 2014',
          title: 'Work',
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-list - misc simple avatar list

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="500"
  >
    <v-toolbar
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Inbox</v-toolbar-title>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-toolbar>
    <v-list>
      <v-list-item
        v-for="item in items"
        :key="item.title"
      >
        <template v-slot:prepend>
          <v-avatar>
            <v-icon
              v-if="item.icon"
              color="pink"
            >
              mdi-star
            </v-icon>
          </v-avatar>
        </template>

        <v-list-item-title>{{ item.title }}</v-list-item-title>

        <template v-slot:append>
          <v-avatar>
            <v-img :src="item.avatar"></v-img>
          </v-avatar>
        </template>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup>
  const items = [
    { icon: true, title: 'Jason Oner', avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg' },
    { title: 'Travis Howard', avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg' },
    { title: 'Ali Connors', avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg' },
    { title: 'Cindy Baker', avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg' },
  ]
</script>

<script>
  export default {
    data () {
      return {
        items: [
          { icon: true, title: 'Jason Oner', avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg' },
          { title: 'Travis Howard', avatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg' },
          { title: 'Ali Connors', avatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg' },
          { title: 'Cindy Baker', avatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg' },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-list - prop three line

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="450"
  >
    <v-toolbar color="cyan-lighten-1">
      <v-btn icon="mdi-menu" variant="text"></v-btn>

      <v-toolbar-title>Inbox</v-toolbar-title>

      <v-btn icon="mdi-magnify" variant="text"></v-btn>
    </v-toolbar>

    <v-list
      :items="items"
      lines="three"
      item-props
    >
      <template v-slot:subtitle="{ subtitle }">
        <div v-html="subtitle"></div>
      </template>
    </v-list>
  </v-card>
</template>

<script setup>
  const items = [
    { type: 'subheader', title: 'Today' },
    {
      prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
      title: 'Brunch this weekend?',
      subtitle: `<span class="text-primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
    },
    { type: 'divider', inset: true },
    {
      prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
      title: 'Summer BBQ',
      subtitle: `<span class="text-primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
    },
    { type: 'divider', inset: true },
    {
      prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
      title: 'Oui oui',
      subtitle: '<span class="text-primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
    },
    { type: 'divider', inset: true },
    {
      prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
      title: 'Birthday gift',
      subtitle: '<span class="text-primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
    },
    { type: 'divider', inset: true },
    {
      prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
      title: 'Recipe to try',
      subtitle: '<span class="text-primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        { type: 'subheader', title: 'Today' },
        {
          prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
          title: 'Brunch this weekend?',
          subtitle: `<span class="text-primary">Ali Connors</span> &mdash; I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`,
        },
        { type: 'divider', inset: true },
        {
          prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
          title: 'Summer BBQ',
          subtitle: `<span class="text-primary">to Alex, Scott, Jennifer</span> &mdash; Wish I could come, but I'm out of town this weekend.`,
        },
        { type: 'divider', inset: true },
        {
          prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
          title: 'Oui oui',
          subtitle: '<span class="text-primary">Sandra Adams</span> &mdash; Do you have Paris recommendations? Have you ever been?',
        },
        { type: 'divider', inset: true },
        {
          prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
          title: 'Birthday gift',
          subtitle: '<span class="text-primary">Trevor Hansen</span> &mdash; Have any ideas about what we should get Heidi for her birthday?',
        },
        { type: 'divider', inset: true },
        {
          prependAvatar: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
          title: 'Recipe to try',
          subtitle: '<span class="text-primary">Britta Holt</span> &mdash; We should eat this: Grate, Squash, Corn, and tomatillo Tacos.',
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-list - misc action stack

Example code

```vue
<template>
  <v-card class="mx-auto" max-width="500">
    <v-toolbar color="pink">
      <v-btn icon="mdi-menu"></v-btn>

      <v-toolbar-title>Inbox</v-toolbar-title>

      <v-btn icon="mdi-magnify"></v-btn>

      <v-btn icon="mdi-checkbox-marked-circle"></v-btn>
    </v-toolbar>

    <v-list v-model:selected="selected" select-strategy="leaf">
      <v-list-item
        v-for="item in items"
        :key="item.id"
        :value="item.id"
        active-class="text-pink"
        class="py-3"
      >
        <v-list-item-title>{{ item.title }}</v-list-item-title>

        <v-list-item-subtitle class="mb-1 text-high-emphasis opacity-100">{{ item.headline }}</v-list-item-subtitle>

        <v-list-item-subtitle class="text-high-emphasis">{{ item.subtitle }}</v-list-item-subtitle>

        <template v-slot:append="{ isSelected }">
          <v-list-item-action class="flex-column align-end">
            <small class="mb-4 text-high-emphasis opacity-60">{{ item.action }}</small>

            <v-spacer></v-spacer>

            <v-icon v-if="isSelected" color="yellow-darken-3">mdi-star</v-icon>

            <v-icon v-else class="opacity-30">mdi-star-outline</v-icon>
          </v-list-item-action>
        </template>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const items = [
    { id: 1, action: '15 min', headline: 'Brunch this weekend?', subtitle: `I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`, title: 'Ali Connors' },
    { id: 2, action: '2 hr', headline: 'Summer BBQ', subtitle: `Wish I could come, but I'm out of town this weekend.`, title: 'me, Scrott, Jennifer' },
    { id: 3, action: '6 hr', headline: 'Oui oui', subtitle: 'Do you have Paris recommendations? Have you ever been?', title: 'Sandra Adams' },
    { id: 4, action: '12 hr', headline: 'Birthday gift', subtitle: 'Have any ideas about what we should get Heidi for her birthday?', title: 'Trevor Hansen' },
    { id: 5, action: '18hr', headline: 'Recipe to try', subtitle: 'We should eat this: Grate, Squash, Corn, and tomatillo Tacos.', title: 'Britta Holt' },
  ]

  const selected = shallowRef([2])
</script>

<script>
  export default {
    data: () => ({
      items: [
        { id: 1, action: '15 min', headline: 'Brunch this weekend?', subtitle: `I'll be in your neighborhood doing errands this weekend. Do you want to hang out?`, title: 'Ali Connors' },
        { id: 2, action: '2 hr', headline: 'Summer BBQ', subtitle: `Wish I could come, but I'm out of town this weekend.`, title: 'me, Scrott, Jennifer' },
        { id: 3, action: '6 hr', headline: 'Oui oui', subtitle: 'Do you have Paris recommendations? Have you ever been?', title: 'Sandra Adams' },
        { id: 4, action: '12 hr', headline: 'Birthday gift', subtitle: 'Have any ideas about what we should get Heidi for her birthday?', title: 'Trevor Hansen' },
        { id: 5, action: '18hr', headline: 'Recipe to try', subtitle: 'We should eat this: Grate, Squash, Corn, and tomatillo Tacos.', title: 'Britta Holt' },
      ],
      selected: [2],
    }),
  }
</script>

```

# Vuetify component v-list - prop items prop

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="300"
  >
    <v-list :items="items"></v-list>
  </v-card>
</template>

<script setup>
  const items = [
    {
      title: 'Item #1',
      value: 1,
      props: {
        prependIcon: 'mdi-home',
      },
    },
    {
      title: 'Item #2',
      value: 2,
      props: {
        appendIcon: 'mdi-close',
      },
    },
    {
      title: 'Item #3',
      value: 3,
      props: {
        color: 'primary',
      },
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          title: 'Item #1',
          value: 1,
          props: {
            prependIcon: 'mdi-home',
          },
        },
        {
          title: 'Item #2',
          value: 2,
          props: {
            appendIcon: 'mdi-close',
          },
        },
        {
          title: 'Item #3',
          value: 3,
          props: {
            color: 'primary',
          },
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-list - misc subheadings and dividers

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="475"
  >
    <v-toolbar
      color="teal"
      dark
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Settings</v-toolbar-title>
    </v-toolbar>

    <v-list lines="two">
      <v-list-subheader>General</v-list-subheader>

      <v-list-item>
        <v-list-item-title>Profile photo</v-list-item-title>
        <v-list-item-subtitle>Change your Google+ profile photo</v-list-item-subtitle>
      </v-list-item>

      <v-list-item>
        <v-list-item-title>Show your status</v-list-item-title>
        <v-list-item-subtitle>Your status is visible to everyone</v-list-item-subtitle>
      </v-list-item>
    </v-list>

    <v-divider></v-divider>

    <v-list v-model="settings" lines="two" select-strategy="leaf">
      <v-list-subheader>Hangout notifications</v-list-subheader>

      <v-list-item>
        <template v-slot:default="{ active, }">
          <v-list-item-action>
            <v-checkbox
              :model-value="active"
              color="primary"
            ></v-checkbox>
          </v-list-item-action>

          <v-list-item-header>
            <v-list-item-title>Notifications</v-list-item-title>
            <v-list-item-subtitle>Allow notifications</v-list-item-subtitle>
          </v-list-item-header>
        </template>
      </v-list-item>

      <v-list-item>
        <template v-slot:default="{ active }">
          <v-list-item-action>
            <v-checkbox
              :model-value="active"
              color="primary"
            ></v-checkbox>
          </v-list-item-action>

          <v-list-item-header>
            <v-list-item-title>Sound</v-list-item-title>
            <v-list-item-subtitle>Hangouts message</v-list-item-subtitle>
          </v-list-item-header>
        </template>
      </v-list-item>

      <v-list-item>
        <template v-slot:default="{ active }">
          <v-list-item-action>
            <v-checkbox
              :model-value="active"
              color="primary"
            ></v-checkbox>
          </v-list-item-action>

          <v-list-item-header>
            <v-list-item-title>Video sounds</v-list-item-title>
            <v-list-item-subtitle>Hangouts video call</v-list-item-subtitle>
          </v-list-item-header>
        </template>
      </v-list-item>

      <v-list-item>
        <template v-slot:default="{ active }">
          <v-list-item-action>
            <v-checkbox
              :model-value="active"
              color="primary"
            ></v-checkbox>
          </v-list-item-action>

          <v-list-item-header>
            <v-list-item-title>Invites</v-list-item-title>
            <v-list-item-subtitle>Notify when receiving invites</v-list-item-subtitle>
          </v-list-item-header>
        </template>
      </v-list-item>
    </v-list>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const settings = ref([])
</script>

<script>
  export default {
    data: () => ({
      settings: [],
    }),
  }
</script>

```

# Vuetify component v-list - prop items type

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="300"
  >
    <v-list :items="items"></v-list>
  </v-card>
</template>

<script setup>
  const items = [
    { type: 'subheader', title: 'Group #1' },
    {
      title: 'Item #1',
      value: 1,
    },
    {
      title: 'Item #2',
      value: 2,
    },
    {
      title: 'Item #3',
      value: 3,
    },
    { type: 'divider' },
    { type: 'subheader', title: 'Group #2' },
    {
      title: 'Item #4',
      value: 4,
    },
    {
      title: 'Item #5',
      value: 5,
    },
    {
      title: 'Item #6',
      value: 6,
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        { type: 'subheader', title: 'Group #1' },
        {
          title: 'Item #1',
          value: 1,
        },
        {
          title: 'Item #2',
          value: 2,
        },
        {
          title: 'Item #3',
          value: 3,
        },
        { type: 'divider' },
        { type: 'subheader', title: 'Group #2' },
        {
          title: 'Item #4',
          value: 4,
        },
        {
          title: 'Item #5',
          value: 5,
        },
        {
          title: 'Item #6',
          value: 6,
        },
      ],
    }),
  }
</script>

```
