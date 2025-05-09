# Vuetify component v-banner - usage

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
      <v-banner
        v-bind="props"
        :avatar="avatar ? 'https://cdn.vuetifyjs.com/images/john-smirk.png' : undefined"
      >
        <template v-slot:text>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Aliquam earum, est illo quae fugit voluptatum fuga magni hic maiores ipsa, illum, tenetur accusamus cupiditate? Dolorem ad nisi eveniet officia voluptatibus.
        </template>

        <template v-if="actions" v-slot:actions>
          <v-btn>Click me</v-btn>
        </template>
      </v-banner>
    </div>

    <template v-slot:configuration>
      <v-select
        v-model="color"
        :items="[
          'success',
          'info',
          'warning',
          'error',
        ]"
        label="Color"
        clearable
      ></v-select>

      <v-checkbox v-model="avatar" label="Avatar"></v-checkbox>

      <v-checkbox v-model="icon" label="Icon"></v-checkbox>

      <v-checkbox v-model="actions" label="Actions"></v-checkbox>

      <v-checkbox v-if="actions" v-model="stacked" label="Stacked"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-banner'
  const model = ref('default')
  const options = ['One line', 'Two lines', 'Three lines']
  const icon = ref(false)
  const avatar = ref(false)
  const actions = ref(false)
  const stacked = ref(false)
  const color = ref()

  const props = computed(() => {
    return {
      avatar: avatar.value ? 'smirk.png' : undefined,
      color: color.value ? color.value : undefined,
      icon: icon.value ? '$vuetify' : undefined,
      lines: model.value !== 'default' ? model.value.toLocaleLowerCase().split(' ')[0] : undefined,
      text: '...',
      stacked: stacked.value,
    }
  })

  const slots = computed(() => {
    return `
  <template v-slot:actions>
    <v-btn>Click me</v-btn>
  </template>
`
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-banner - slot icon

Example code

```vue
<template>
  <v-banner
    color="pink-darken-1"
    icon="mdi-account-box"
    lines="two"
  >
    <template v-slot:prepend>
      <v-avatar></v-avatar>
    </template>

    <v-banner-text>
      Banner with two lines of text. If the text is too long to fit on two lines then an ellipsis will be used to hide the remaining content. So this next line will be hidden.
    </v-banner-text>

    <v-banner-actions>
      <v-btn>Action Button</v-btn>
    </v-banner-actions>
  </v-banner>
</template>

```

# Vuetify component v-banner - slot prepend

Example code

```vue
<template>
  <v-banner
    color="deep-purple-accent-4"
    lines="two"
  >
    <template v-slot:prepend>
      <v-avatar
        color="deep-purple-accent-4"
        icon="mdi-account-filter"
      ></v-avatar>
    </template>

    <v-banner-text>
      Banner with two lines of text. If the text is too long to fit on two lines then an ellipsis will be used to hide the remaining content. So this next line will be hidden.
    </v-banner-text>

    <v-banner-actions>
      <v-btn>Action</v-btn>

      <v-btn>Action</v-btn>
    </v-banner-actions>
  </v-banner>
</template>

```

# Vuetify component v-banner - prop sticky

Example code

```vue
<template>
  <v-card
    class="overflow-auto mx-auto"
    max-height="300"
    width="448"
  >
    <v-toolbar color="primary">
      <v-toolbar-title>My Document</v-toolbar-title>

      <template v-slot:append>
        <v-switch
          v-model="sticky"
          color="secondary"
          label="Sticky Banner"
          hide-details
        ></v-switch>
      </template>
    </v-toolbar>

    <v-banner
      :sticky="sticky"
      lines="one"
    >
      <template v-slot:text>
        We can't save your edits while you are in offline mode.
      </template>

      <template v-slot:actions>
        <v-btn color="deep-purple-accent-4">
          Go Online
        </v-btn>
      </template>
    </v-banner>

    <v-card-text class="bg-grey-lighten-4">
      <v-sheet
        class="mx-auto"
        height="300"
      ></v-sheet>
    </v-card-text>

    <v-footer
      class="justify-center"
      color="primary"
    >
      End of Content
    </v-footer>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const sticky = ref(false)
</script>

<script>
  export default {
    data: () => ({
      sticky: false,
    }),
  }
</script>

```

# Vuetify component v-banner - prop lines

Example code

```vue
<template>
  <div>
    <v-banner
      class="my-4"
      color="deep-purple-accent-4"
      icon="mdi-lock"
      lines="one"
    >
      <v-banner-text>
        Banner with one line of text.
      </v-banner-text>

      <template v-slot:actions>
        <v-btn>Action</v-btn>
      </template>
    </v-banner>

    <v-banner
      class="my-4"
      color="error"
      icon="mdi-weather-hurricane"
      lines="two"
    >
      <v-banner-text>
        Banner with two lines of text. If the text is too long to fit on two lines then an ellipsis will be used to hide the remaining content. So this next line will be hidden.
      </v-banner-text>

      <template v-slot:actions>
        <v-btn>Action</v-btn>
      </template>
    </v-banner>

    <v-banner
      class="my-4"
      color="warning"
      icon="$warning"
      lines="three"
    >
      <v-banner-text>
        Banner with three lines of text. One or two lines is preferable. Three lines should be considered the absolute maximum length on desktop in order to keep messages short and actionable.
      </v-banner-text>

      <template v-slot:actions>
        <v-btn>Action</v-btn>
      </template>
    </v-banner>
  </div>
</template>

```

# Vuetify component v-banner - slot actions

Example code

```vue
<template>
  <v-banner
    color="warning"
    icon="mdi-wifi-strength-alert-outline"
    lines="one"
  >
    <template v-slot:text>
      No Internet connection
    </template>

    <template v-slot:actions>
      <v-btn>
        Dismiss
      </v-btn>

      <v-btn>
        Retry
      </v-btn>
    </template>
  </v-banner>
</template>

```
