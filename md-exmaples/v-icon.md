# Vuetify component v-icon - usage

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
      <v-icon v-bind="props"></v-icon>
    </div>

    <template v-slot:configuration>
      <v-select v-model="size" :items="sizes" label="Size"></v-select>

      <v-select v-model="color" :items="colors" label="Color"></v-select>

      <v-select v-model="icon" :items="icons" label="Icon" clearable></v-select>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-icon'
  const model = ref('default')
  const icon = ref()
  const size = ref()
  const color = ref()
  const options = []
  const props = computed(() => {
    return {
      color: color.value || undefined,
      icon: icon.value || '$vuetify',
      size: ['', 'medium'].includes(size.value) ? undefined : size.value,
    }
  })
  const colors = [
    'success',
    'info',
    'warning',
    'error',
  ]
  const icons = [
    'mdi-plus',
    'mdi-check-circle',
    'mdi-information',
    'mdi-alert',
    'mdi-alert-circle',
    'mdi-wifi',
    'mdi-access-point',
    'mdi-antenna',
  ]
  const sizes = [
    'x-small',
    'small',
    'medium',
    'large',
    'x-large',
  ]

  const slots = computed(() => {
    return ``
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-icon - misc md

Example code

```vue
<template>
  <div class="d-flex justify-space-around">
    <v-icon icon="md:home"></v-icon>
    <v-icon icon="md:event"></v-icon>
    <v-icon icon="md:info"></v-icon>
    <v-icon icon="md:folder_open"></v-icon>
    <v-icon icon="md:widgets"></v-icon>
    <v-icon icon="md:gavel"></v-icon>
  </div>
</template>

```

# Vuetify component v-icon - misc mdi svg

Example code

```vue
<template>
  <div class="d-flex justify-space-around">
    <v-icon :icon="`mdiSvg:${mdiAccount}`"></v-icon>
    <v-icon :icon="`mdiSvg:${mdiPencil}`"></v-icon>
    <v-icon :icon="`mdiSvg:${mdiShareVariant}`"></v-icon>
    <v-icon :icon="`mdiSvg:${mdiDelete}`"></v-icon>
  </div>
</template>

<script setup>
  import { mdiAccount, mdiDelete, mdiPencil, mdiShareVariant } from '@mdi/js'
</script>

<script>
  import {
    mdiAccount,
    mdiDelete,
    mdiPencil,
    mdiShareVariant,
  } from '@mdi/js'

  export default {
    data: () => ({
      mdiAccount,
      mdiPencil,
      mdiShareVariant,
      mdiDelete,
    }),
  }
</script>

```

# Vuetify component v-icon - prop color

Example code

```vue
<template>
  <v-row justify="space-around">
    <v-icon
      color="green-darken-2"
      icon="mdi-domain"
      size="large"
    ></v-icon>

    <v-icon
      color="blue-darken-2"
      icon="mdi-message-text"
      size="large"
    ></v-icon>

    <v-icon
      color="purple-darken-2"
      icon="mdi-dialpad"
      size="large"
    ></v-icon>

    <v-icon
      color="teal-darken-2"
      icon="mdi-email"
      size="large"
    ></v-icon>

    <v-icon
      color="blue-grey-darken-2"
      icon="mdi-call-split"
      size="large"
    ></v-icon>

    <v-icon
      color="orange-darken-2"
      icon="mdi-arrow-up-bold-box-outline"
      size="large"
    ></v-icon>
  </v-row>
</template>

```

# Vuetify component v-icon - misc buttons

Example code

```vue
<template>
  <div class="text-center">
    <div>
      <v-btn
        class="ma-2"
        color="primary"
      >
        Accept
        <v-icon
          icon="mdi-checkbox-marked-circle"
          end
        ></v-icon>
      </v-btn>

      <v-btn
        class="ma-2"
        color="red"
      >
        Decline
        <v-icon
          icon="mdi-cancel"
          end
        ></v-icon>
      </v-btn>

      <v-btn
        class="ma-2"
      >
        <v-icon
          icon="mdi-minus-circle"
          start
        ></v-icon>
        Cancel
      </v-btn>
    </div>

    <div>
      <v-btn
        class="ma-2"
        color="orange-darken-2"
      >
        <v-icon
          icon="mdi-arrow-left"
          start
        ></v-icon>
        Back
      </v-btn>

      <v-btn
        class="ma-2"
        color="purple"
        icon="mdi-wrench"
      ></v-btn>

      <v-btn
        class="ma-2"
        color="indigo"
        icon="mdi-cloud-upload"
      ></v-btn>
    </div>

    <div>
      <v-btn
        class="ma-2"
        color="blue-lighten-2"
        icon="mdi-thumb-up"
        variant="text"
      ></v-btn>

      <v-btn
        class="ma-2"
        color="red-lighten-2"
        icon="mdi-thumb-down"
        variant="text"
      ></v-btn>
    </div>
  </div>
</template>

```

# Vuetify component v-icon - misc font awesome

Example code

```vue
<template>
  <div class="d-flex justify-space-around">
    <v-icon icon="fa:fas fa-lock"></v-icon>

    <v-icon icon="fa:fas fa-search"></v-icon>

    <v-icon icon="fa:fas fa-list"></v-icon>

    <v-icon icon="fa:fas fa-edit"></v-icon>

    <v-icon icon="fa:fas fa-tachometer-alt"></v-icon>

    <v-icon icon="fa:fas fa-circle-notch fa-spin"></v-icon>
  </div>
</template>

<playground-resources lang="json">
  {
    "css": ["https://use.fontawesome.com/releases/v5.1.0/css/all.css"]
  }
</playground-resources>

```

# Vuetify component v-icon - event click

Example code

```vue
<template>
  <v-card>
    <v-toolbar
      color="pink"
      dark
      dense
      flat
    >
      <v-toolbar-title class="text-body-2">
        Upcoming Changes
      </v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-icon
        size="large"
        @click="next"
      >
        mdi-chevron-right
      </v-icon>
    </v-card-actions>
  </v-card>
</template>

<script setup>
  function next () {
    alert('You clicked next!')
  }
</script>

<script>
  export default {
    methods: {
      next () {
        alert('You clicked next!')
      },
    },
  }
</script>

```
