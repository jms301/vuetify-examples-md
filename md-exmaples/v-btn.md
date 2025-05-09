# Vuetify component v-btn - usage

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
      <v-btn v-bind="props">
        <template v-if="!icon" v-slot:default>Button</template>
      </v-btn>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="icon" label="Icon"></v-checkbox>
      <v-checkbox v-model="prepend" label="Prepend icon"></v-checkbox>
      <v-checkbox v-model="append" label="Append icon"></v-checkbox>
      <v-checkbox v-model="stacked" label="Stacked"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const variants = ['outlined', 'tonal', 'text', 'plain']
  const name = 'v-btn'
  const model = ref('default')
  const icon = ref(false)
  const options = [...variants]
  const block = ref(false)
  const stacked = ref(false)
  const prepend = ref(false)
  const append = ref(false)
  const props = computed(() => {
    return {
      block: block.value || undefined,
      'prepend-icon': prepend.value ? '$vuetify' : undefined,
      'append-icon': append.value ? '$vuetify' : undefined,
      icon: icon.value ? '$vuetify' : undefined,
      stacked: stacked.value || undefined,
      variant: variants.includes(model.value) ? model.value : undefined,
    }
  })

  watch(stacked, val => {
    if (val) {
      prepend.value = true
      append.value = false
      icon.value = false
    }
  })

  watch(prepend, val => {
    if (val) {
      icon.value = false

      if (stacked.value) (append.value = false)
    }
  })

  watch(append, val => {
    if (val) {
      icon.value = false

      if (stacked.value) (prepend.value = false)
    }
  })
  watch(icon, val => val && (prepend.value = false, append.value = false, stacked.value = false))

  const slots = computed(() => {
    return `
  Button
`
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-btn - prop ripple

Example code

```vue
<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="auto">
        <v-btn
          height="72"
          min-width="164"
        >
          With Ripple
        </v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn
          :ripple="false"
          height="72"
          min-width="164"
        >
          Without Ripple
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-btn - prop variant

Example code

```vue
<template>
  <div class="d-flex justify-space-between">
    <v-btn>elevated (default)</v-btn>
    <v-btn variant="flat">flat</v-btn>
    <v-btn variant="tonal">tonal</v-btn>
    <v-btn variant="outlined">outlined</v-btn>
    <v-btn variant="text">text</v-btn>
    <v-btn variant="plain">plain</v-btn>
  </div>
</template>

```

# Vuetify component v-btn - prop rounded

Example code

```vue
<template>
  <v-container class="text-center">
    <v-row justify="center">
      <v-col cols="12" md="4" sm="6">
        <v-btn rounded="0" size="x-large" block>Rounded 0</v-btn>
      </v-col>

      <v-col cols="12" md="4" sm="6">
        <v-btn rounded="xs" size="x-large" block>Rounded xs</v-btn>
      </v-col>

      <v-col cols="12" md="4" sm="6">
        <v-btn rounded="sm" size="x-large" block>Rounded sm</v-btn>
      </v-col>

      <v-col cols="12" md="4" sm="6">
        <v-btn size="x-large" block>Button</v-btn>
      </v-col>

      <v-col cols="12" md="4" sm="6">
        <v-btn rounded="lg" size="x-large" block>Rounded lg</v-btn>
      </v-col>

      <v-col cols="12" md="4" sm="6">
        <v-btn rounded="xl" size="x-large" block>Rounded xl</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-btn - misc group survey

Example code

```vue
<template>
  <v-card
    class="px-2 mx-auto"
    max-width="300"
    rounded="lg"
    text="How satisfied are you with developing using Vuetify?"
    theme="dark"
    title="SURVEY"
    variant="flat"
  >
    <template v-slot:append>
      <div class="me-n2">
        <v-btn
          density="comfortable"
          icon="$close"
          variant="plain"
        ></v-btn>
      </div>
    </template>

    <v-item-group
      v-model="model"
      class="d-flex justify-sm-space-between px-6 pt-2 pb-6"
    >
      <v-item
        v-for="n in 5"
        :key="n"
      >
        <template v-slot:default="{ toggle }">
          <v-btn
            :active="model != null && model + 1 >= n"
            :icon="`mdi-numeric-${n}`"
            height="40"
            variant="text"
            width="40"
            border
            @click="toggle"
          ></v-btn>
        </template>
      </v-item>
    </v-item-group>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const model = ref(null)
</script>

<script>
  export default {
    data: () => ({
      model: null,
    }),
  }
</script>

```

# Vuetify component v-btn - prop icon

Example code

```vue
<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="auto">
        <v-btn density="compact" icon="mdi-plus"></v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn density="comfortable" icon="$vuetify"></v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn density="default" icon="mdi-open-in-new"></v-btn>
      </v-col>
    </v-row>

    <v-row align="center" justify="center">
      <v-col cols="auto">
        <v-btn icon="mdi-account" size="x-small"></v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn icon="mdi-plus" size="small"></v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn icon="$vuetify"></v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn icon="mdi-open-in-new" size="large"></v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn icon="mdi-calendar" size="x-large"></v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-btn - prop size

Example code

```vue
<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="auto">
        <v-btn size="x-small">Extra small Button</v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn size="small">Small Button</v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn>Regular Button</v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn size="large">Large Button</v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn size="x-large">X-Large Button</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-btn - prop density

Example code

```vue
<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="auto">
        <v-btn density="compact">Compact Button</v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn density="comfortable">Comfortable Button</v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn density="default">Default Button</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-btn - prop block

Example code

```vue
<template>
  <v-btn block>Block Button</v-btn>
</template>

```

# Vuetify component v-btn - prop floating

Example code

```vue
<template>
  <div class="text-center">
    <v-btn
      class="mx-2"
      color="primary"
      size="small"
      icon
    >
      <v-icon>
        mdi-minus
      </v-icon>
    </v-btn>

    <v-btn
      class="mx-2"
      color="pink"
      size="small"
      icon
    >
      <v-icon>
        mdi-heart
      </v-icon>
    </v-btn>

    <v-btn
      class="mx-2"
      color="indigo"
      icon
    >
      <v-icon>
        mdi-plus
      </v-icon>
    </v-btn>

    <v-btn
      class="mx-2"
      color="teal"
      icon
    >
      <v-icon>
        mdi-format-list-bulleted-square
      </v-icon>
    </v-btn>

    <v-btn
      class="mx-2"
      color="cyan"
      size="large"
      icon
    >
      <v-icon>
        mdi-pencil
      </v-icon>
    </v-btn>

    <v-btn
      class="mx-2"
      color="purple"
      size="large"
      icon
    >
      <v-icon>
        mdi-android
      </v-icon>
    </v-btn>
  </div>
</template>

```

# Vuetify component v-btn - prop elevation

Example code

```vue
<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col class="text-center" cols="12">
        <v-btn size="x-large">Default Elevation (2)</v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn elevation="4" size="x-large">Elevation 4</v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn elevation="8" size="x-large">Elevation 8</v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn elevation="12" size="x-large">Elevation 12</v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn elevation="16" size="x-large">Elevation 16</v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn elevation="20" size="x-large">Elevation 20</v-btn>
      </v-col>

      <v-col cols="auto">
        <v-btn elevation="24" size="x-large">Elevation 24</v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify component v-btn - misc tax form

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    elevation="1"
    max-width="500"
  >
    <v-card-title class="py-5 font-weight-black">Securely access your tax form</v-card-title>

    <v-card-text>
      To download your tax form from GitHub Sponsors on Stripe Express, you must also verify the Tax ID number used on your tax forms, as they contain sensitive personal information.
    </v-card-text>

    <v-card-text>
      <div class="text-subtitle-2 font-weight-black mb-1">Last 4 digits of your SSN</div>

      <v-text-field
        label="Enter value here"
        variant="outlined"
        single-line
      ></v-text-field>

      <v-btn
        :disabled="loading"
        :loading="loading"
        class="text-none mb-4"
        color="indigo-darken-3"
        size="x-large"
        variant="flat"
        block
        @click="loading = !loading"
      >
        Verify and continue
      </v-btn>

      <v-btn
        class="text-none"
        color="grey-lighten-3"
        size="x-large"
        variant="flat"
        block
      >
        Cancel
      </v-btn>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { ref, watch } from 'vue'

  const loading = ref(false)

  watch(loading, val => {
    if (!val) return
    setTimeout(() => (loading.value = false), 2000)
  })
</script>

<script>
  export default {
    data: () => ({
      loading: false,
    }),

    watch: {
      loading (val) {
        if (!val) return

        setTimeout(() => (this.loading = false), 2000)
      },
    },
  }
</script>

```

# Vuetify component v-btn - defaults snackbar

Example code

```vue
<template>
  <v-sheet
    class="position-relative"
    min-height="100"
  >
    <div class="position-absolute d-flex align-center justify-center w-100 h-100">
      <v-btn
        size="x-large"
        @click="snackbar = !snackbar"
      >
        Toggle Snackbar
      </v-btn>
    </div>

    <v-snackbar
      v-model="snackbar"
      location="center"
    >
      Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!

      <template v-slot:actions>
        <v-btn @click="onClick">Close</v-btn>
      </template>
    </v-snackbar>
  </v-sheet>
</template>

<script setup>
  import { ref } from 'vue'

  const snackbar = ref(false)

  function onClick () {
    snackbar.value = false
  }
</script>

<script>
  export default {
    data: () => ({
      snackbar: false,
    }),

    methods: {
      onClick () {
        this.snackbar = false
      },
    },
  }
</script>

```

# Vuetify component v-btn - prop loaders

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="450"
    text="Update your weak or re-used passwords with Password Checkup. It's free and only takes a few minutes. Click the Take Checkup button to get started."
    title="Strengthen your passwords"
  >

    <template v-slot:actions>
      <v-btn height="48">
        No Thanks
      </v-btn>

      <v-btn
        :loading="loading"
        class="flex-grow-1"
        height="48"
        variant="tonal"
        @click="load"
      >
        Take Checkup
      </v-btn>
    </template>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const loading = ref(false)
  function load () {
    loading.value = true
    setTimeout(() => (loading.value = false), 3000)
  }
</script>

<script>
  export default {
    data: () => ({ loading: false }),

    methods: {
      load () {
        this.loading = true
        setTimeout(() => (this.loading = false), 3000)
      },
    },
  }
</script>

```

# Vuetify component v-btn - misc readonly

Example code

```vue
<template>
  <v-list-item
    base-color="surface-light"
    border="opacity-50 md"
    lines="two"
    max-width="796"
    prepend-avatar="https://cdn.vuetifyjs.com/docs/images/one/logos/one.png"
    rounded="lg"
    variant="flat"
  >
    <v-list-item-title>
      <span class="text-h6">Vuetify One Subscriber</span>
    </v-list-item-title>

    <v-list-item-subtitle :opacity="isSubscriber ? .8 : undefined">
      <v-scroll-y-reverse-transition mode="out-in">
        <div
          v-if="isSubscriber"
          key="subscribed"
          class="text-success text-caption"
        >
          <v-icon icon="mdi-medal" size="1em"></v-icon>
          $2.99 /month
        </div>

        <div
          v-else
          key="not-subscribed"
          class="text-caption"
        >
          Support Vuetify by becoming a Subscriber
        </div>
      </v-scroll-y-reverse-transition>
    </v-list-item-subtitle>

    <template v-slot:append>
      <v-fade-transition mode="out-in">
        <v-btn
          :key="`subscribe-${isSubscriber}`"
          :border="`thin ${isSubscriber ? 'error' : 'success'}`"
          :color="isSubscriber ? 'error' : 'success'"
          :prepend-icon="isSubscriber ? 'mdi-close' : 'mdi-email'"
          :slim="isSubscriber"
          :text="isSubscriber ? 'Cancel' : 'Subscribe'"
          :variant="isSubscriber ? 'plain' : 'tonal'"
          class="me-2 text-none"
          size="small"
          @click="isSubscriber = !isSubscriber"
        ></v-btn>
      </v-fade-transition>

      <v-fade-transition mode="out-in">
        <v-btn
          :key="`info-${isSubscriber}`"
          :color="isSubscriber ? 'success' : 'primary'"
          :prepend-icon="isSubscriber ? 'mdi-check' : 'mdi-open-in-new'"
          :readonly="isSubscriber"
          :text="isSubscriber ? 'Subscribed' : 'More Info'"
          class="text-none"
          size="small"
          variant="flat"
        ></v-btn>
      </v-fade-transition>
    </template>
  </v-list-item>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const isSubscriber = shallowRef(false)
</script>

```

# Vuetify component v-btn - defaults banner actions

Example code

```vue
<template>
  <v-banner
    lines="one"
  >
    <template v-slot:text>
      Banner with one line of text.
    </template>

    <template v-slot:actions>
      <v-btn>
        Action
      </v-btn>

      <v-btn>
        Action
      </v-btn>
    </template>
  </v-banner>
</template>

```

# Vuetify component v-btn - prop flat

Example code

```vue
<template>
  <div class="d-flex justify-space-around align-center flex-column flex-sm-row fill-height">
    <v-btn variant="flat">
      Normal
    </v-btn>

    <v-btn
      color="secondary"
      variant="flat"
    >
      Secondary
    </v-btn>

    <v-btn
      color="error"
      variant="flat"
    >
      Error
    </v-btn>

    <v-btn
      variant="flat"
      disabled
    >
      Disabled
    </v-btn>
  </div>
</template>

```

# Vuetify component v-btn - slot loader

Example code

```vue
<template>
  <div class="text-center">
    <v-btn
      :loading="loading"
      @click="loading = !loading"
    >
      Custom loader

      <template v-slot:loader>
        <v-progress-linear indeterminate></v-progress-linear>
      </template>
    </v-btn>
  </div>
</template>

<script setup>
  import { ref, watch } from 'vue'

  const loading = ref(false)
  watch(loading, val => {
    if (!val) return
    setTimeout(() => (loading.value = false), 2000)
  })
</script>

<script>
  export default {
    data: () => ({
      loading: false,
    }),

    watch: {
      loading (val) {
        if (!val) return

        setTimeout(() => (this.loading = false), 2000)
      },
    },
  }
</script>

```

# Vuetify component v-btn - prop outlined

Example code

```vue
<template>
  <div class="d-flex justify-space-around align-center flex-column flex-sm-row">
    <v-btn
      color="primary"
      variant="outlined"
    >
      Outlined Button
    </v-btn>
    <v-btn
      color="secondary"
      variant="outlined"
      icon
    >
      <v-icon>mdi-format-list-bulleted-square</v-icon>
    </v-btn>
    <v-btn
      color="info"
      size="large"
      variant="outlined"
      icon
    >
      <v-icon>mdi-pencil</v-icon>
    </v-btn>
  </div>
</template>

```

# Vuetify component v-btn - prop tile

Example code

```vue
<template>
  <v-row
    align="center"
    justify="space-around"
  >
    <v-btn
      color="success"
      tile
    >
      <v-icon start>
        mdi-pencil
      </v-icon>
      Edit
    </v-btn>
  </v-row>
</template>

```

# Vuetify component v-btn - misc raised

Example code

```vue
<template>
  <v-row
    align="center"
    justify="space-around"
  >
    <v-btn>Normal</v-btn>
    <v-btn color="primary">
      Primary
    </v-btn>
    <v-btn color="error">
      Error
    </v-btn>
    <v-btn disabled>
      Disabled
    </v-btn>
  </v-row>
</template>

```

# Vuetify component v-btn - defaults bottom navigation

Example code

```vue
<template>
  <v-layout
    class="overflow-visible"
    style="height: 56px;"
  >
    <v-bottom-navigation
      v-model="value"
      active
    >
      <v-btn>Home</v-btn>

      <v-btn>Recents</v-btn>

      <v-btn>Favorites</v-btn>
    </v-bottom-navigation>
  </v-layout>
</template>

<script setup>
  import { ref } from 'vue'

  const value = ref(0)
</script>

<script>
  export default {
    data: () => ({ value: 0 }),
  }
</script>

```

# Vuetify component v-btn - misc discord event

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    color="#36393f"
    max-width="650"
    min-height="350"
    theme="dark"
    variant="flat"
  >
    <v-sheet color="#202225">
      <v-card-item>
        <template v-slot:prepend>
          <v-card-title>
            <v-icon
              icon="mdi-calendar"
              start
            ></v-icon>

            1 Event
          </v-card-title>
        </template>

        <v-divider class="mx-2" vertical></v-divider>

        <v-btn
          class="text-none text-subtitle-1"
          color="#5865f2"
          size="small"
          variant="flat"
        >
          Create Event
        </v-btn>

        <template v-slot:append>
          <v-btn
            icon="$close"
            size="large"
            variant="text"
          ></v-btn>
        </template>
      </v-card-item>
    </v-sheet>

    <v-card
      class="ma-4"
      color="#2f3136"
      rounded="lg"
      variant="flat"
    >
      <v-card-item>
        <v-card-title class="text-body-2 d-flex align-center">
          <v-icon
            color="#949cf7"
            icon="mdi-calendar"
            start
          ></v-icon>

          <span class="text-medium-emphasis font-weight-bold">1 Fri Dec 16th - 9:00 PM</span>

          <v-spacer></v-spacer>

          <v-avatar
            image="https://cdn.vuetifyjs.com/images/john-smirk.png"
            size="x-small"
          ></v-avatar>

          <v-chip
            class="ms-2 text-medium-emphasis"
            color="grey-darken-4"
            prepend-icon="mdi-account-multiple"
            size="small"
            text="81"
            variant="flat"
          ></v-chip>
        </v-card-title>

        <div class="py-2">
          <div class="text-h6">Live Q&A</div>

          <div class="font-weight-light text-medium-emphasis">
            Join the Vuetify team for a live Question and Answer session.
          </div>
        </div>
      </v-card-item>

      <v-divider></v-divider>

      <div class="pa-4 d-flex align-center">
        <v-icon
          color="disabled"
          icon="mdi-broadcast"
          start
        ></v-icon>

        <v-icon
          color="#949cf7"
          icon="mdi-video-vintage"
          size="x-small"
        ></v-icon>

        <span class="text-caption text-medium-emphasis ms-1 font-weight-light">
          streaming
        </span>

        <v-spacer></v-spacer>

        <v-btn
          icon="mdi-dots-horizontal"
          variant="text"
        ></v-btn>

        <v-btn
          class="me-2 text-none"
          color="#4f545c"
          prepend-icon="mdi-export-variant"
          variant="flat"
        >
          Share
        </v-btn>

        <v-btn
          class="text-none"
          prepend-icon="mdi-check"
          variant="text"
          border
        >
          Interested
        </v-btn>
      </div>
    </v-card>
  </v-card>
</template>

```

# Vuetify component v-btn - prop plain

Example code

```vue
<template>
  <div class="d-flex justify-space-around">
    <v-btn
      color="grey"
      variant="plain"
    >
      Cancel
    </v-btn>

    <v-btn
      color="error"
      variant="plain"
    >
      Delete
    </v-btn>
  </div>
</template>

```

# Vuetify component v-btn - defaults toolbar

Example code

```vue
<template>
  <v-toolbar title="Toolbar">
    <v-toolbar-items>
      <v-btn>Dashboard</v-btn>

      <v-btn>Resources</v-btn>
    </v-toolbar-items>

    <v-divider class="mx-2" vertical></v-divider>

    <v-btn icon="mdi-dots-vertical"></v-btn>
  </v-toolbar>
</template>

```

# Vuetify component v-btn - misc cookie settings

Example code

```vue
<template>
  <v-banner
    avatar="https://cdn.vuetifyjs.com/docs/images/logos/v.svg"
    stacked
  >
    <template v-slot:text>
      Vuetify uses cookies to enable and import the use of the website. Please see our <a href="https://www.iubenda.com/privacy-policy/76325752/cookie-policy" target="_blank">Privacy Policy</a> for more information. By clicking "Accept Cookies" or continuing to use the site, you agree to the use of cookies.
    </template>

    <template v-slot:actions>
      <v-dialog v-model="dialog" max-width="500">
        <template v-slot:activator="{ props }">
          <v-btn
            class="text-none"
            color="blue-darken-4"
            rounded="0"
            variant="outlined"
            v-bind="props"
          >
            Manage Cookies
          </v-btn>
        </template>

        <v-card title="Cookie Settings">
          <v-card-text>
            <p class="pb-4">
              Vuetify websites use cookies to deliver and improve the visitor experience. Learn more about the cookies we use on our Cookie Policy page.
            </p>

            <v-list-subheader class="font-weight-black text-high-emphasis">Required Cookies</v-list-subheader>

            <p class="mb-4">These cookies are required for the site to function and cannot be turned off.</p>

            <v-list-subheader class="font-weight-black text-high-emphasis">Performance Cookies</v-list-subheader>

            <v-switch
              v-model="performance"
              :label="performance ? 'On' : 'Off'"
              color="blue-darken-4"
              density="compact"
              hide-details
              inline
              inset
            ></v-switch>

            <p class="mb-4">Counts website visits and clicks to understand where people most engage with links to make the experience better.</p>

            <v-list-subheader class="font-weight-black text-high-emphasis">Advertising Cookies</v-list-subheader>

            <v-switch
              v-model="advertising"
              :label="advertising ? 'On' : 'Off'"
              color="blue-darken-4"
              density="compact"
              hide-details
              inline
              inset
            ></v-switch>

            <p class="mb-16">Set by our advertising partners, these cookies are used to build a profile of your interests and show you relevant ads on other sites. They do not store personal information, but are based on uniquely identifying your browser and internet device.</p>
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions class="justify-center px-6 py-3">
            <v-btn
              class="flex-grow-1 text-none"
              color="blue-darken-4"
              rounded="0"
              variant="plain"
              @click="dialog=false"
            >
              Decline All
            </v-btn>

            <v-btn
              class="text-white flex-grow-1 text-none"
              color="blue-darken-4"
              rounded="0"
              variant="flat"
              @click="dialog=false"
            >
              Save and Accept
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>

      <v-btn
        class="text-none ms-4 text-white"
        color="blue-darken-4"
        rounded="0"
        variant="flat"
      >
        Accept Cookies
      </v-btn>
    </template>
  </v-banner>
</template>

<script setup>
  import { ref } from 'vue'

  const dialog = ref(false)
  const advertising = ref(true)
  const performance = ref(true)
</script>

<script>
  export default {
    data: () => ({
      dialog: false,
      advertising: true,
      performance: true,
    }),
  }
</script>

```

# Vuetify component v-btn - slot prepend append

Example code

```vue
<template>
  <div class="text-center">
    <v-btn
      append-icon="mdi-account-circle"
      prepend-icon="mdi-check-circle"
    >
      <template v-slot:prepend>
        <v-icon color="success"></v-icon>
      </template>

      Button

      <template v-slot:append>
        <v-icon color="warning"></v-icon>
      </template>
    </v-btn>
  </div>
</template>

```

# Vuetify component v-btn - misc dialog action

Example code

```vue
<template>
  <v-sheet
    class="position-relative"
    min-height="450"
  >
    <div class="position-absolute d-flex align-center justify-center w-100 h-100">
      <v-btn
        color="deep-purple-darken-2"
        size="x-large"
        @click="dialog = !dialog"
      >
        Open Dialog
      </v-btn>
    </div>

    <v-fade-transition hide-on-leave>
      <v-card
        v-if="dialog"
        append-icon="$close"
        class="mx-auto"
        elevation="16"
        max-width="500"
        title="Send a receipt"
      >
        <template v-slot:append>
          <v-btn icon="$close" variant="text" @click="dialog = false"></v-btn>
        </template>

        <v-divider></v-divider>

        <div class="py-12 text-center">
          <v-icon
            class="mb-6"
            color="success"
            icon="mdi-check-circle-outline"
            size="128"
          ></v-icon>

          <div class="text-h4 font-weight-bold">This receipt was sent</div>
        </div>

        <v-divider></v-divider>

        <div class="pa-4 text-end">
          <v-btn
            class="text-none"
            color="medium-emphasis"
            min-width="92"
            variant="outlined"
            rounded
            @click="dialog = false"
          >
            Close
          </v-btn>
        </div>
      </v-card>
    </v-fade-transition>
  </v-sheet>
</template>

<script setup>
  import { ref } from 'vue'

  const dialog = ref(true)
</script>

```

# Vuetify component v-btn - misc toolbar

Example code

```vue
<template>
  <v-toolbar>
    <template v-slot:prepend>
      <v-btn icon="mdi-arrow-left"></v-btn>
    </template>

    <v-btn class="ms-5" icon="mdi-archive-plus-outline"></v-btn>

    <v-btn icon="mdi-alert-circle-outline"></v-btn>

    <v-btn icon="mdi-delete-outline"></v-btn>

    <template v-if="$vuetify.display.smAndUp">
      <v-divider
        class="mx-3 align-self-center"
        length="24"
        thickness="2"
        vertical
      ></v-divider>

      <v-btn icon="mdi-folder-outline"></v-btn>

      <v-btn icon="mdi-tag-outline"></v-btn>

      <v-btn icon="mdi-dots-vertical"></v-btn>
    </template>
  </v-toolbar>
</template>

```

# Vuetify component v-btn - defaults card actions

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="500"
    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!"
    title="Card title"
  >
    <v-card-actions>
      <v-btn>Action Button</v-btn>
    </v-card-actions>
  </v-card>
</template>

```

# Vuetify component v-btn - defaults btn group

Example code

```vue
<template>
  <div class="d-flex align-center flex-column pa-6">
    <v-btn-group
      variant="outlined"
      divided
    >
      <v-btn icon="mdi-format-align-left"></v-btn>
      <v-btn icon="mdi-format-align-center"></v-btn>
      <v-btn icon="mdi-format-align-right"></v-btn>
      <v-btn icon="mdi-format-align-justify"></v-btn>
    </v-btn-group>
  </div>
</template>

```
