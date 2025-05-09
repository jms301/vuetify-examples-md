# Vuetify component v-badge - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <div class="text-center">
      <v-badge v-bind="props">
        <v-icon
          icon="$vuetify"
          size="x-large"
        ></v-icon>
      </v-badge>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="dot" label="Dot"></v-checkbox>

      <v-slider
        v-model="content"
        label="Value"
        max="100"
        min="0"
        step="1"
      ></v-slider>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-badge'
  const model = ref('default')
  const content = ref(0)
  const dot = ref(false)
  const options = ['floating', 'inline']
  const props = computed(() => {
    return {
      content: content.value || undefined,
      dot: dot.value || undefined,
      floating: model.value === 'floating' || undefined,
      inline: model.value === 'inline' || undefined,
    }
  })

  const slots = computed(() => {
    return `
  <v-icon icon="$vuetify" size="x-large"></v-icon>
`
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-badge - misc dynamic

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <div>
        <v-btn
          class="mx-1"
          color="primary"
          @click="messages++"
        >
          Send Message
        </v-btn>

        <v-btn
          class="mx-1"
          color="error"
          @click="messages = 0"
        >
          Clear Notifications
        </v-btn>
      </div>

      <v-badge
        :content="messages"
        :model-value="!!messages"
        color="green"
      >
        <v-icon size="large">
          $vuetify
        </v-icon>
      </v-badge>
    </v-row>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const messages = ref(0)
</script>

<script>
  export default {
    data () {
      return {
        messages: 0,
      }
    },
  }
</script>

```

# Vuetify component v-badge - prop inline

Example code

```vue
<template>
  <v-list
    class="mx-auto"
    max-width="256"
    border
  >
    <v-list-item
      prepend-icon="mdi-inbox-arrow-down"
      title="Inbox"
      link
    >
      <template v-slot:append>
        <v-badge
          color="error"
          content="6"
          inline
        ></v-badge>
      </template>
    </v-list-item>

    <v-list-item
      prepend-icon="mdi-send"
      title="Sent Mail"
      link
    ></v-list-item>

    <v-list-item
      prepend-icon="mdi-delete"
      title="Trash"
      link
    >
      <template v-slot:append>
        <v-badge
          color="info"
          content="12"
          inline
        ></v-badge>
      </template>
    </v-list-item>

    <v-list-item
      prepend-icon="mdi-alert-circle"
      title="Spam"
      link
    ></v-list-item>
  </v-list>
</template>

```

# Vuetify component v-badge - misc customization

Example code

```vue
<template>
  <div class="d-flex justify-space-around align-center flex-column flex-md-row fill-height">
    <v-badge
      color="error"
      icon="mdi-lock"
      bordered
    >
      <v-btn
        color="error"
        variant="flat"
      >
        Lock Account
      </v-btn>
    </v-badge>

    <v-badge
      color="deep-purple-accent-4"
      location="bottom end"
      offset-x="2"
      offset-y="4"
      bordered
      dot
    >
      <v-avatar size="large">
        <v-img src="https://cdn.vuetifyjs.com/images/lists/2.jpg"></v-img>
      </v-avatar>
    </v-badge>

    <div class="mx-3"></div>

    <v-badge
      bordered
    >
      <template v-slot:badge>
        <v-avatar size="x-small">
          <v-img src="https://cdn.vuetifyjs.com/images/logos/v.png"></v-img>
        </v-avatar>
      </template>

      <v-avatar size="large">
        <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
      </v-avatar>
    </v-badge>
  </div>
</template>

```

# Vuetify component v-badge - prop content

Example code

```vue
<template>
  <v-toolbar color="blue-grey-darken-3">
    <v-spacer></v-spacer>

    <v-btn class="text-none" stacked>
      <v-badge color="success" dot>
        <v-icon>mdi-home-outline</v-icon>
      </v-badge>
    </v-btn>

    <v-btn class="text-none" stacked>
      <v-icon>mdi-account-multiple-outline</v-icon>
    </v-btn>

    <v-btn class="text-none" stacked>
      <v-badge color="error" content="9+">
        <v-icon>mdi-store-outline</v-icon>
      </v-badge>
    </v-btn>

    <v-btn class="text-none" stacked>
      <v-badge color="error" content="2">
        <v-icon>mdi-bell-outline</v-icon>
      </v-badge>
    </v-btn>

    <v-btn class="text-none" stacked>
      <v-icon>mdi-menu</v-icon>
    </v-btn>

    <v-spacer></v-spacer>
  </v-toolbar>
</template>

```

# Vuetify component v-badge - misc tabs

Example code

```vue
<template>
  <v-tabs
    bg-color="primary"
    grow
  >
    <v-tab>
      <v-badge
        color="pink"
        dot
      >
        Item One
      </v-badge>
    </v-tab>

    <v-tab>
      <v-badge
        color="green"
        content="6"
      >
        Item Two
      </v-badge>
    </v-tab>

    <v-tab>
      <v-badge
        color="deep-purple-accent-4"
        icon="$vuetify"
      >
        Item Three
      </v-badge>
    </v-tab>
  </v-tabs>
</template>

```

# Vuetify component v-badge - prop dot

Example code

```vue
<template>
  <v-toolbar color="grey-lighten-3" title="Application">
    <v-btn stacked>
      <v-badge
        color="error"
        dot
      >
        <v-icon icon="mdi-newspaper-variant-outline"></v-icon>
      </v-badge>

      News
    </v-btn>

    <v-btn stacked>
      <v-badge
        color="error"
        dot
      >
        <v-icon icon="mdi-post"></v-icon>
      </v-badge>

      Blog
    </v-btn>

    <v-btn
      variant="tonal"
      stacked
    >
      <v-icon icon="mdi-login"></v-icon>

      Login
    </v-btn>
  </v-toolbar>
</template>

```

# Vuetify component v-badge - misc hover

Example code

```vue
<template>
  <div class="text-center">
    <v-badge
      :model-value="hover"
      color="deep-purple"
      content="9999+"
      location="top-end"
      transition="slide-x-transition"
    >
      <v-hover v-slot="{ props }" v-model="hover">
        <v-icon
          color="grey-lighten-1"
          size="large"
          v-bind="props"
        >
          mdi-account
        </v-icon>
      </v-hover>
    </v-badge>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const hover = ref(false)
</script>

<script>
  export default {
    data: () => ({
      hover: false,
    }),
  }
</script>

```
