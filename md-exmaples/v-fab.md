# Vuetify component v-fab - usage

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
      <v-fab v-bind="props"></v-fab>
    </div>

    <template v-slot:configuration>
      <v-select
        v-model="color"
        :items="items"
        label="Color"
        clearable
      ></v-select>
      <v-checkbox v-model="extended" label="Extended"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const variants = ['outlined', 'tonal', 'flat', 'text', 'plain']
  const name = 'v-fab'
  const model = shallowRef('default')
  const options = [...variants]
  const extended = shallowRef(false)
  const color = shallowRef()
  const items = ['primary', 'success', 'surface-variant']

  const props = computed(() => {
    return {
      color: color.value || undefined,
      extended: extended.value || undefined,
      icon: !extended.value ? '$vuetify' : undefined,
      'prepend-icon': extended.value ? '$vuetify' : undefined,
      text: extended.value ? 'Extended' : undefined,
      variant: variants.includes(model.value) ? model.value : undefined,
    }
  })

  const slots = computed(() => {
    return ''
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-fab - misc small

Example code

```vue
<template>
  <v-card class="mx-auto" max-width="365">
    <v-toolbar
      color="light-blue"
      extended
      light
    >
      <v-app-bar-nav-icon color="grey-darken-4"></v-app-bar-nav-icon>

      <v-toolbar-title>My files</v-toolbar-title>

      <v-btn color="grey-darken-4" icon="mdi-magnify"></v-btn>

      <v-btn color="grey-darken-4" icon="mdi-view-module"></v-btn>

      <template v-slot:extension>
        <v-fab
          class="ms-4"
          color="cyan-accent-2"
          icon="mdi-plus"
          location="bottom left"
          size="40"
          absolute
          offset
          @click="dialog = !dialog"
        ></v-fab>
      </template>
    </v-toolbar>

    <v-list lines="two">
      <v-list-subheader title="Folders" inset></v-list-subheader>

      <v-list-item
        v-for="item in items"
        :key="item.title"
        link
      >
        <template v-slot:prepend>
          <v-avatar :class="[item.iconClass]" :icon="item.icon"></v-avatar>
        </template>

        <v-list-item-title>{{ item.title }}</v-list-item-title>

        <v-list-item-subtitle>{{ item.subtitle }}</v-list-item-subtitle>

        <template v-slot:append>
          <v-list-item-action>
            <v-btn color="grey-lighten-1" icon="mdi-information" variant="text"></v-btn>
          </v-list-item-action>
        </template>
      </v-list-item>

      <v-divider inset></v-divider>

      <v-list-subheader title="Files" inset></v-list-subheader>

      <v-list-item
        v-for="item in items2"
        :key="item.title"
        link
      >
        <template v-slot:prepend>
          <v-avatar :class="[item.iconClass]" :icon="item.icon"></v-avatar>
        </template>

        <v-list-item-title>{{ item.title }}</v-list-item-title>

        <v-list-item-subtitle>{{ item.subtitle }}</v-list-item-subtitle>

        <template v-slot:append>
          <v-list-item-action>
            <v-btn color="grey-lighten-1" icon="mdi-information" variant="text"></v-btn>
          </v-list-item-action>
        </template>
      </v-list-item>
    </v-list>

    <v-dialog
      v-model="dialog"
      max-width="500"
    >
      <v-card>
        <v-card-text>
          <v-text-field label="File name"></v-text-field>

          <small class="text-grey">* This doesn't actually save.</small>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn
            color="primary"
            variant="text"
            @click="dialog = false"
          >
            Submit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const dialog = ref(false)
  const items = ref([
    { icon: 'mdi-folder', iconClass: 'bg-grey-lighten-1 text-white', title: 'Photos', subtitle: 'Jan 9, 2014' },
    { icon: 'mdi-folder', iconClass: 'bg-grey-lighten-1 text-white', title: 'Recipes', subtitle: 'Jan 17, 2014' },
    { icon: 'mdi-folder', iconClass: 'bg-grey-lighten-1 text-white', title: 'Work', subtitle: 'Jan 28, 2014' },
  ])
  const items2 = ref([
    { icon: 'mdi-clipboard-text', iconClass: 'bg-blue text-white', title: 'Vacation itinerary', subtitle: 'Jan 20, 2014' },
    { icon: 'mdi-gesture-tap-button', iconClass: 'bg-amber text-white', title: 'Kitchen remodel', subtitle: 'Jan 10, 2014' },
  ])
</script>

```

# Vuetify component v-fab - misc speed dial

Example code

```vue
<template>
  <v-app>
    <v-card class="pa-6 mb-6" variant="flat">
      <v-row dense>
        <v-col cols="12" sm="3">
          <h5>FAB position</h5>

          <v-radio-group v-model="fabPosition" density="compact" hide-details>
            <v-radio label="App (fixed)" value="fixed"></v-radio>
            <v-radio label="Absolute" value="absolute"></v-radio>
            <v-radio label="None" value=""></v-radio>
          </v-radio-group>
        </v-col>

        <v-col cols="12" sm="3">
          <h5>FAB location</h5>

          <v-radio-group v-model="fabLocation" :disabled="!fabPosition" density="compact" hide-details>
            <div class="d-flex">
              <v-radio value="top left"></v-radio>
              <v-radio value="top center"></v-radio>
              <v-radio value="top right"></v-radio>
            </div>

            <div class="d-flex">
              <v-radio value="left center"></v-radio>
              <v-radio :disabled="fabPosition !== 'absolute'" value="center center"></v-radio>
              <v-radio value="right center"></v-radio>
            </div>

            <div class="d-flex">
              <v-radio value="left bottom"></v-radio>
              <v-radio value="bottom center"></v-radio>
              <v-radio value="right bottom"></v-radio>
            </div>
          </v-radio-group>

          <code>({{ fabLocation }})</code>
        </v-col>

        <v-col cols="12" sm="3">
          <h5>Menu location</h5>

          <v-radio-group v-model="menuLocation" density="compact" hide-details>
            <div class="d-flex">
              <v-radio disabled></v-radio>
              <v-radio value="top left"></v-radio>
              <v-radio value="top center"></v-radio>
              <v-radio value="top right"></v-radio>
              <v-radio disabled></v-radio>
            </div>

            <div class="d-flex">
              <v-radio value="left top"></v-radio>
              <v-radio disabled></v-radio>
              <v-radio disabled></v-radio>
              <v-radio disabled></v-radio>
              <v-radio value="right top"></v-radio>
            </div>

            <div class="d-flex">
              <v-radio value="left center"></v-radio>
              <v-radio disabled></v-radio>
              <v-radio value="center"></v-radio>
              <v-radio disabled></v-radio>
              <v-radio value="right center"></v-radio>
            </div>

            <div class="d-flex">
              <v-radio value="left bottom"></v-radio>
              <v-radio disabled></v-radio>
              <v-radio disabled></v-radio>
              <v-radio disabled></v-radio>
              <v-radio value="right bottom"></v-radio>
            </div>

            <div class="d-flex">
              <v-radio disabled></v-radio>
              <v-radio value="bottom left"></v-radio>
              <v-radio value="bottom center"></v-radio>
              <v-radio value="bottom right"></v-radio>
              <v-radio disabled></v-radio>
            </div>
          </v-radio-group>

          <code>({{ menuLocation }})</code>
        </v-col>

        <v-col cols="12" sm="3">
          <h5>Transition</h5>

          <v-radio-group v-model="transition" density="compact" hide-details>
            <v-radio label="Fade" value="fade-transition"></v-radio>
            <v-radio label="Slide y" value="slide-y-transition"></v-radio>
            <v-radio label="Slide y reverse" value="slide-y-reverse-transition"></v-radio>
            <v-radio label="Slide x" value="slide-x-transition"></v-radio>
            <v-radio label="Slide x reverse" value="slide-x-reverse-transition"></v-radio>
            <v-radio label="Scale" value="scale-transition"></v-radio>
          </v-radio-group>
        </v-col>
      </v-row>
    </v-card>

    <v-card :class="fabPosition === 'absolute' ? 'demo-panel-relative' : 'demo-panel-static'" border flat>
      <v-fab
        :key="fabPosition"
        :absolute="fabPosition === 'absolute'"
        :app="fabPosition === 'fixed'"
        :color="open ? '' : 'primary'"
        :location="fabLocation"
        size="large"
        icon
      >
        <v-icon>{{ open ? 'mdi-close' : 'mdi-crown' }}</v-icon>
        <v-speed-dial v-model="open" :location="menuLocation" :transition="transition" activator="parent">
          <v-btn key="1" color="success" icon>
            <v-icon size="24">$success</v-icon>
          </v-btn>

          <v-btn key="2" color="info" icon>
            <v-icon size="24">$info</v-icon>
          </v-btn>

          <v-btn key="3" color="warning" icon>
            <v-icon size="24">$warning</v-icon>
          </v-btn>

          <v-btn key="4" color="error" icon>
            <v-icon size="24">$error</v-icon>
          </v-btn>
        </v-speed-dial>
      </v-fab>
    </v-card>
  </v-app>
</template>

<script setup>
  import { shallowRef, watch } from 'vue'

  const open = shallowRef(false)
  const fabPosition = shallowRef('absolute')
  const menuLocation = shallowRef('left center')
  const fabLocation = shallowRef('right bottom')
  const transition = shallowRef('slide-y-reverse-transition')

  watch(menuLocation, reopen)
  watch(transition, reopen)
  watch(fabLocation, () => open.value = false)
  watch(fabPosition, () => open.value = false)

  function reopen () {
    open.value = false
    setTimeout(() => open.value = true, 400)
  }
</script>

<style scoped>
/* This is for documentation purposes and will not be needed in your application */
::v-deep(.v-application__wrap) {
  min-height: 0 !important;
}

.demo-panel-static,
.demo-panel-relative {
  margin: 0 80px 50px;
  padding: 24px;
  min-height: 300px;
}
.demo-panel-static {
  position: static;
}
.demo-panel-relative {
  position: relative;
}

.v-selection-control--disabled,
.v-input--disabled .v-selection-control {
  opacity: .1;
}

.v-radio {
  flex-grow: 0 !important;
}

h5 {
  margin-bottom: 12px;
}

code {
  display: block;
  font-size: .8rem;
  margin-top: 12px;
}

::v-deep(.v-label) {
  margin-left: 8px;
}
</style>

```

# Vuetify component v-fab - misc display animation

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="360"
  >
    <v-layout>
      <v-app-bar absolute extended>
        <v-app-bar-nav-icon></v-app-bar-nav-icon>

        <template v-slot:extension>
          <v-fab
            :active="!hidden"
            class="ms-4"
            icon="mdi-plus"
            location="bottom start"
            size="small"
            absolute
            offset
          ></v-fab>
        </template>
      </v-app-bar>

      <v-main>
        <v-sheet class="pa-4 text-center" color="surface-light" height="300">
          <v-btn
            :text="hidden ? 'Show' : 'Hide'"
            color="surface-variant"
            width="80"
            @click="hidden = !hidden"
          >
          </v-btn>
        </v-sheet>

        <v-sheet height="125">
          <v-fab
            :active="!hidden"
            class="me-4"
            icon="mdi-plus"
            location="top end"
            absolute
            offset
          ></v-fab>
        </v-sheet>
      </v-main>
    </v-layout>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const hidden = ref(false)
</script>

<script>
  export default {
    data: () => ({
      hidden: false,
    }),
  }
</script>

```

# Vuetify component v-fab - misc lateral screens

Example code

```vue
<template>
  <v-card>
    <v-layout>
      <v-app-bar
        color="indigo"
        absolute
        flat
      >
        <v-app-bar-nav-icon></v-app-bar-nav-icon>

        <v-app-bar-title>Page title</v-app-bar-title>

        <v-btn icon="mdi-magnify"></v-btn>

        <v-btn icon="mdi-dots-vertical">
          <v-icon></v-icon>
        </v-btn>

        <template v-slot:extension>
          <v-tabs
            v-model="tabs"
            align-tabs="title"
            slider-color="pink"
          >
            <v-tab text="Item One" value="one"></v-tab>

            <v-tab text="Item Two" value="two"></v-tab>

            <v-tab text="Item Three" value="three"></v-tab>
          </v-tabs>
        </template>
      </v-app-bar>

      <v-main>
        <v-sheet height="150"></v-sheet>
      </v-main>

      <v-fab
        :key="activeFab.icon"
        :color="activeFab.color"
        :icon="activeFab.icon"
        class="ms-4 mb-4"
        location="bottom start"
        size="64"
        absolute
        app
        appear
      ></v-fab>
    </v-layout>
  </v-card>
</template>

<script setup>
  import { computed, ref } from 'vue'

  const tabs = ref(null)
  const activeFab = computed(() => {
    switch (tabs.value) {
      case 'one': return { color: 'success', icon: 'mdi-share-variant' }
      case 'two': return { color: 'red', icon: 'mdi-pencil' }
      case 'three': return { color: 'green', icon: 'mdi-chevron-up' }
      default: return {}
    }
  })
</script>

<script>
  export default {
    data: () => ({
      tabs: null,
    }),

    computed: {
      activeFab () {
        switch (this.tabs) {
          case 'one': return { color: 'success', icon: 'mdi-share-variant' }
          case 'two': return { color: 'red', icon: 'mdi-pencil' }
          case 'three': return { color: 'green', icon: 'mdi-chevron-up' }
          default: return {}
        }
      },
    },
  }
</script>

```
