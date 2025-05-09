# Vuetify component v-icon-btn - usage

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
      <v-icon-btn v-bind="props" v-ripple="ripple"></v-icon-btn>
    </div>

    <template v-slot:configuration>
      <v-select
        v-model="color"
        :items="['primary', 'secondary', 'accent', 'error', 'warning', 'info', 'success']"
        label="Color"
        clearable
      ></v-select>

      <v-select
        v-model="size"
        :items="['x-small', 'small', 'default', 'large', 'x-large']"
        label="Size"
        clearable
      ></v-select>

      <v-select
        v-model="icon"
        :items="['$vuetify', 'mdi-lightning-bolt', 'mdi-account-outline', 'mdi-cog-outline', 'mdi-heart-outline']"
        :list-props="{ slim: true }"
        label="Icon"
      >
        <template v-slot:item="{ props: itemProps, item }">
          <v-list-item v-bind="itemProps" :prepend-icon="item.title"></v-list-item>
        </template>
      </v-select>

      <v-checkbox-btn v-model="loading" label="Loading"></v-checkbox-btn>

      <v-checkbox-btn v-model="hideOverlay" label="Hide overlay"></v-checkbox-btn>

      <v-checkbox-btn v-model="ripple" label="Ripple"></v-checkbox-btn>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const variants = ['outlined', 'tonal', 'flat', 'text', 'plain']
  const name = 'v-icon-btn'
  const model = shallowRef('default')
  const color = shallowRef()
  const hideOverlay = shallowRef(false)
  const icon = shallowRef('$vuetify')
  const ripple = shallowRef(false)
  const loading = shallowRef(false)
  const size = shallowRef('default')
  const options = [...variants]
  const props = computed(() => {
    return {
      color: color.value || undefined,
      'hide-overlay': hideOverlay.value || undefined,
      icon: icon.value || undefined,
      loading: loading.value || undefined,
      size: size.value !== 'default' ? size.value : undefined,
      variant: model.value !== 'default' ? model.value : undefined,
      'v-ripple': ripple.value || undefined,
    }
  })

  const slots = computed(() => {
    return ``
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-icon-btn - prop active

Example code

```vue
<template>
  <v-toolbar class="px-3 mx-auto" rounded="pill" title="Toolbar">
    <template v-slot:append>
      <v-icon-btn :active="menu" active-color="surface-variant" icon="mdi-dots-vertical">
        <v-icon></v-icon>

        <v-menu v-model="menu" activator="parent" location="bottom end" offset="4">
          <v-list
            bg-color="surface-light"
            class="d-flex flex-column ga-1 pa-1"
            density="compact"
            rounded="lg"
            variant="text"
            slim
          >
            <v-list-item
              prepend-icon="mdi-account-circle-outline"
              rounded="lg"
              title="Account"
              link
            ></v-list-item>

            <v-list-item
              prepend-icon="mdi-cog-outline"
              rounded="lg"
              title="Settings"
              link
            ></v-list-item>

            <v-list-item
              prepend-icon="mdi-logout-variant"
              rounded="lg"
              title="Logout"
              link
            ></v-list-item>
          </v-list>
        </v-menu>
      </v-icon-btn>
    </template>
  </v-toolbar>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const menu = shallowRef(false)
</script>

<script>
  export default {
    data () {
      return {
        menu: false,
      }
    },
  }
</script>

```

# Vuetify component v-icon-btn - misc table actions

Example code

```vue
<template>
  <v-container>
    <v-sheet border>
      <v-data-table :headers="headers" :items="plants" hide-default-footer>
        <template v-slot:item.color="{ item }">
          <v-chip
            :text="item.color"
            color="medium-emphasis"
            size="small"
            border
          >
            <template v-slot:prepend>
              <v-avatar
                :color="item.color.toLowerCase()"
                border="thin opacity-25"
                size="16"
                start
              ></v-avatar>
            </template>
          </v-chip>
        </template>

        <template v-slot:item.actions="{ item, index }">
          <div class="d-flex ga-2 justify-end">
            <v-icon-btn
              icon="mdi-pencil"
              size="24"
              variant="plain"
              @click="onClickEdit(item)"
            >
              <v-icon size="16"></v-icon>
            </v-icon-btn>

            <v-icon-btn
              icon="mdi-delete-outline"
              size="24"
              variant="plain"
              @click="onClickDelete(index)"
            >
              <v-icon size="16"></v-icon>
            </v-icon-btn>
          </div>
        </template>

        <template v-slot:no-data>
          <v-btn
            prepend-icon="mdi-backup-restore"
            rounded="lg"
            text="Reset data"
            variant="text"
            border
            @click="onClickReset"
          ></v-btn>
        </template>
      </v-data-table>
    </v-sheet>

    <v-dialog
      v-model="dialog"
      max-width="450"
      @after-leave="onAfterLeave"
    >
      <v-card density="compact" title="Edit">
        <v-divider></v-divider>

        <v-card-text>
          <v-text-field
            v-model="record.title"
            density="compact"
            label="Title"
            variant="outlined"
            rounded
          ></v-text-field>

          <v-text-field
            v-model="record.color"
            density="compact"
            label="Color"
            variant="outlined"
            rounded
          ></v-text-field>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions class="bg-surface-light">
          <v-spacer></v-spacer>

          <v-icon-btn
            :loading="isSaving"
            color="primary"
            icon="mdi-content-save"
            variant="flat"
            @click="onClickSave"
          ></v-icon-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script setup>
  import { ref, shallowRef } from 'vue'

  const DEFAULT_RECORD = () => ({ title: '', color: '' })
  const DEFAULT_RECORDS = () => ([
    { id: 1, title: '🌹 Rose', color: 'Red' },
    { id: 2, title: '🌷 Tulip', color: 'Yellow' },
    { id: 3, title: '🌻 Sunflower', color: 'Yellow' },
    { id: 4, title: '🌼 Daisy', color: 'White' },
    { id: 5, title: '🥀 Orchid', color: 'Purple' },
  ])

  const isSaving = shallowRef(false)
  const dialog = shallowRef(false)
  const record = shallowRef(DEFAULT_RECORD())

  const headers = [
    { title: 'Title', align: 'start', key: 'title' },
    { title: 'Color', align: 'end', key: 'color' },
    { title: 'Actions', align: 'end', key: 'actions' },
  ]

  const plants = ref(DEFAULT_RECORDS())

  function onAfterLeave () {
    record.value = DEFAULT_RECORD()
  }

  function onClickDelete (index) {
    plants.value.splice(index, 1)
  }

  function onClickEdit (item) {
    dialog.value = true
    record.value = { ...item }
  }

  function onClickReset () {
    plants.value = DEFAULT_RECORDS()
  }

  async function onClickSave () {
    isSaving.value = true

    await new Promise(resolve => setTimeout(resolve, 1000))

    const index = plants.value.findIndex(plant => plant.id === record.value.id)

    plants.value[index] = { ...record.value }

    dialog.value = false
    isSaving.value = false
  }
</script>

<script>
  export default {
    data () {
      return {
        isSaving: false,
        dialog: false,
        record: { title: '', color: '' },
        plants: [
          { id: 1, title: '🌹 Rose', color: 'Red' },
          { id: 2, title: '🌷 Tulip', color: 'Yellow' },
          { id: 3, title: '🌻 Sunflower', color: 'Yellow' },
          { id: 4, title: '🌼 Daisy', color: 'White' },
          { id: 5, title: '🥀 Orchid', color: 'Purple' },
        ],
        headers: [
          { title: 'Title', align: 'start', key: 'title' },
          { title: 'Color', align: 'end', key: 'color' },
          { title: 'Actions', align: 'end', key: 'actions' },
        ],
      }
    },
    methods: {
      defaultRecord () {
        return { title: '', color: '' }
      },
      defaultRecords () {
        return [
          { id: 1, title: '🌹 Rose', color: 'Red' },
          { id: 2, title: '🌷 Tulip', color: 'Yellow' },
          { id: 3, title: '🌻 Sunflower', color: 'Yellow' },
          { id: 4, title: '🌼 Daisy', color: 'White' },
          { id: 5, title: '🥀 Orchid', color: 'Purple' },
        ]
      },
      onAfterLeave () {
        this.record = this.defaultRecord()
      },
      onClickDelete (index) {
        this.plants.splice(index, 1)
      },
      onClickEdit (item) {
        this.dialog = true
        this.record = { ...item }
      },
      onClickReset () {
        this.plants = this.defaultRecords()
      },
      async onClickSave () {
        this.isSaving = true
        await new Promise(resolve => setTimeout(resolve, 1000))

        const index = this.plants.findIndex(plant => plant.id === this.record.id)
        this.plants[index] = { ...this.record }

        this.dialog = false
        this.isSaving = false
      },
    },
  }
</script>

```

# Vuetify component v-icon-btn - prop opacity

Example code

```vue
<template>
  <v-text-field
    class="mx-auto"
    hide-details="auto"
    label="Search"
    max-width="200"
    variant="outlined"
  >
    <template v-slot:append-inner>
      <v-icon-btn
        :opacity="dialog ? 1 : 0.32"
        icon="mdi-magnify"
        @click.stop
        @mousedown.stop
      >
        <v-icon></v-icon>

        <v-dialog v-model="dialog" activator="parent" width="400">
          <v-card title="Find in page">
            <v-card-text>
              <v-text-field hide-details="auto" label="Search"></v-text-field>
            </v-card-text>

            <template v-slot:actions>
              <v-btn text="Cancel" variant="plain" @click="dialog = false"></v-btn>

              <v-btn text="Search" @click="dialog = false"></v-btn>
            </template>
          </v-card>
        </v-dialog>
      </v-icon-btn>
    </template>
  </v-text-field>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const dialog = shallowRef(false)
</script>

<script>
  export default {
    data () {
      return {
        dialog: false,
      }
    },
  }
</script>

```

# Vuetify component v-icon-btn - misc markdown editor

Example code

```vue
<template>
  <v-container class="pa-md-12">
    <v-card
      class="mx-auto"
      color="blue-grey-darken-2"
      max-width="640"
      rounded="lg"
      variant="tonal"
    >
      <v-toolbar
        density="compact"
        rounded="t-lg"
        title="Editor"
        border
      >
        <template v-slot:append>
          <div class="d-flex align-center pa-1">
            <div ref="desktopTarget"></div>

            <v-icon-btn
              v-if="display.mobile.value"
              icon="mdi-dots-vertical"
              rounded="lg"
              size="32"
            >
              <v-icon></v-icon>

              <v-menu activator="parent" width="200">
                <v-card rounded="lg">
                  <div ref="mobileTarget"></div>
                </v-card>
              </v-menu>
            </v-icon-btn>
          </div>
        </template>
      </v-toolbar>

      <div class="px-4 pb-4">
        <v-textarea
          ref="textarea"
          v-model="model"
          variant="plain"
          auto-grow
          hide-details
        ></v-textarea>

        <input
          ref="images"
          class="d-none"
          type="file"
          multiple
        >
      </div>
    </v-card>

    <Teleport v-if="teleportTarget" :to="teleportTarget">
      <div class="d-flex ga-2 pa-2 flex-wrap justify-space-between">
        <template v-for="(item, i) in actions" :key="i">
          <v-icon-btn
            v-if="!item.divider"
            v-bind="item"
            rounded="lg"
            size="32"
          ></v-icon-btn>

          <v-divider v-else-if="!display.mobile.value" class="mx-1" vertical></v-divider>
        </template>
      </div>
    </Teleport>
  </v-container>
</template>

<script setup>
  import { computed, nextTick, ref, shallowRef } from 'vue'
  import { useDisplay } from 'vuetify'

  const display = useDisplay()

  const images = ref()
  const textarea = ref()
  const mobileTarget = ref()
  const desktopTarget = ref()
  const model = shallowRef('')
  const teleportTarget = computed(() => display.mobile.value ? mobileTarget.value : desktopTarget.value)

  function onClickHeading () {
    if (!model.value) {
      model.value = '# '
    } else if (model.value === '# ') {
      model.value = ''
    } else {
      model.value += ' # '
    }

    textarea.value.focus()
  }

  async function onClickBold () {
    textarea.value.focus()

    if (!model.value) {
      model.value = '**'
      await nextTick()
      textarea.value.setSelectionRange(1, 1)
    } else if (model.value === '**') {
      model.value = ''
    } else {
      const start = model.value.length
      model.value += ' **'
      await nextTick()
      textarea.value.setSelectionRange(start + 2, start + 2)
    }
  }

  async function onClickItalic () {
    textarea.value.focus()

    if (!model.value) {
      model.value = '__'
      await nextTick()
      textarea.value.setSelectionRange(1, 1)
    } else if (model.value === '__') {
      model.value = ''
    } else {
      const start = model.value.length
      model.value += ' __'
      await nextTick()
      textarea.value.setSelectionRange(start + 2, start + 2)
    }
  }

  function onClickListNumbered () {
    if (!model.value) {
      model.value = '1. '
    } else if (model.value === '1. ') {
      model.value = ''
    } else {
      model.value += ' 1. '
    }

    textarea.value.focus()
  }

  function onClickListUnordered () {
    if (!model.value) {
      model.value = '- '
    } else if (model.value === '- ') {
      model.value = ''
    } else {
      model.value += ' - '
    }

    textarea.value.focus()
  }

  function onClickListTask () {
    if (!model.value) {
      model.value = '- [] '
    } else {
      model.value += '\n\n- [] '
    }

    textarea.value.focus()
  }

  function onClickAttachFiles () {
    images.value.click()
  }

  async function onClickDetails () {
    textarea.value.focus()

    if (!model.value.startsWith('<details>')) {
      model.value = `<details>\n<summary>Details</summary>\n\n\n\n</details>`
      await nextTick()
      textarea.value.setSelectionRange(38, 38)
    } else {
      model.value = ''
    }
  }

  const actions = [
    { icon: 'mdi-format-header-1', onClick: onClickHeading },
    { icon: 'mdi-format-bold', onClick: onClickBold },
    { icon: 'mdi-format-italic', onClick: onClickItalic },
    { divider: true },
    { icon: 'mdi-format-list-numbered', onClick: onClickListNumbered },
    { icon: 'mdi-format-list-bulleted', onClick: onClickListUnordered },
    { icon: 'mdi-format-list-checks', onClick: onClickListTask },
    { divider: true },
    { icon: 'mdi-paperclip', onClick: onClickAttachFiles },
    { divider: true },
    { icon: 'mdi-format-vertical-align-bottom', onClick: onClickDetails },
  ]
</script>

```

# Vuetify component v-icon-btn - prop rotate

Example code

```vue
<template>
  <div class="text-center">
    <v-menu>
      <template v-slot:activator="{ props: activatorProps, isActive }">
        <v-btn v-bind="activatorProps" text="Toggle">
          <template v-slot:append>
            <v-icon-btn
              :rotate="isActive ? 180 : 0"
              icon="$dropdown"
              size="16"
              variant="plain"
              hide-overlay
            ></v-icon-btn>
          </template>
        </v-btn>
      </template>

      <v-list>
        <v-list-item title="Item 1" link></v-list-item>
        <v-list-item title="Item 2" link></v-list-item>
        <v-list-item title="Item 3" link></v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

```

# Vuetify component v-icon-btn - misc dialog

Example code

```vue
<template>
  <div class="text-center">
    <v-btn>
      Open Dialog

      <v-dialog v-model="dialog" activator="parent" max-width="500" persistent>
        <v-card subtitle="Click the X to close" title="Dialog">
          <template v-slot:append>
            <v-icon-btn icon="$close" @click="dialog = false"></v-icon-btn>
          </template>
        </v-card>
      </v-dialog>
    </v-btn>
  </div>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const dialog = shallowRef(false)
</script>

<script>
  export default {
    data () {
      return {
        dialog: false,
      }
    },
  }
</script>

```

# Vuetify component v-icon-btn - misc video controls

Example code

```vue
<template>
  <v-container class="pa-md-12 text-center">
    <v-sheet
      class="d-inline-flex ga-1 pa-4 align-center justify-center mx-auto"
      color="surface-light"
      rounded="pill"
    >
      <v-sheet
        :rounded="!mic ? 'lg' : 'xl'"
        class="overflow-visible d-flex align-center"
        color="surface"
        height="48"
        width="88"
        flat
      >
        <v-icon-btn
          v-model:active="micOptions"
          :active-variant="!mic ? 'flat' : 'text'"
          :base-variant="!mic ? 'flat' : 'text'"
          :color="!mic ? 'error' : ''"
          :rotate="micOptions ? 180 : 0"
          :rounded="!mic ? 'lg' : 'circle'"
          icon="mdi-chevron-up"
          size="48"
          hide-overlay
        ></v-icon-btn>

        <v-icon-btn
          v-model:active="mic"
          :rounded="!mic ? 'lg' : 'circle'"
          active-color=""
          active-icon="mdi-microphone"
          active-variant="tonal"
          base-variant="flat"
          class="ms-n2"
          color="#f9dedc"
          icon="mdi-microphone-off"
          size="48"
          v-ripple
        ></v-icon-btn>
      </v-sheet>

      <v-sheet
        :rounded="!video ? 'lg' : 'xl'"
        class="overflow-visible d-flex align-center"
        color="surface"
        height="48"
        width="88"
        flat
      >
        <v-icon-btn
          v-model:active="videoOptions"
          :active-variant="!video ? 'flat' : 'text'"
          :base-variant="!video ? 'flat' : 'text'"
          :color="!video ? 'error' : ''"
          :rotate="videoOptions ? 180 : 0"
          :rounded="!video ? 'lg' : 'circle'"
          icon="mdi-chevron-up"
          size="48"
          hide-overlay
        ></v-icon-btn>

        <v-icon-btn
          v-model:active="video"
          :rounded="!video ? 'lg' : 'circle'"
          active-color=""
          active-icon="mdi-video-outline"
          active-variant="tonal"
          base-variant="flat"
          class="ms-n2"
          color="#f9dedc"
          icon="mdi-video-off"
          size="48"
        ></v-icon-btn>
      </v-sheet>

      <v-icon-btn
        v-model:active="caption"
        :class="!caption ? 'mx-1' : undefined"
        :rounded="!caption ? 'circle' : 'lg'"
        :width="caption ? 56 : 48"
        active-color="#9bbbef"
        active-icon="mdi-closed-caption"
        active-variant="flat"
        height="48"
        icon="mdi-closed-caption-outline"
      ></v-icon-btn>

      <v-icon-btn
        v-model:active="emoji"
        :class="!emoji ? 'mx-1' : undefined"
        :rounded="!emoji ? 'circle' : 'lg'"
        :width="emoji ? 56 : 48"
        active-color="#9bbbef"
        active-icon="mdi-emoticon"
        height="48"
        icon="mdi-emoticon-outline"
      ></v-icon-btn>

      <v-icon-btn
        v-model:active="share"
        :class="!share ? 'mx-1' : undefined"
        :rounded="!share ? 'circle' : 'lg'"
        :width="share ? 56 : 48"
        active-color="#9bbbef"
        active-icon="mdi-arrow-up-bold-box"
        height="48"
        icon="mdi-arrow-up-bold-box-outline"
        @click="onClick"
      ></v-icon-btn>

      <v-icon-btn
        v-model:active="raised"
        :class="!raised ? 'mx-1' : undefined"
        :rounded="!raised ? 'circle' : 'lg'"
        :width="raised ? 56 : 48"
        active-color="#9bbbef"
        active-icon="mdi-hand-back-right"
        height="48"
        icon="mdi-hand-back-right-outline"
      ></v-icon-btn>

      <v-icon-btn
        height="48"
        icon="mdi-dots-vertical"
        rounded="xl"
        variant="tonal"
      >
        <v-icon></v-icon>

        <v-menu activator="parent" location="top end" offset="4">
          <v-list rounded="lg" slim>
            <v-list-item
              prepend-icon="mdi-radiobox-marked"
              title="Manage recording"
              link
            ></v-list-item>

            <v-divider class="my-2"></v-divider>

            <v-list-item
              prepend-icon="mdi-view-grid-outline"
              title="Change layout"
              link
            ></v-list-item>

            <v-list-item
              prepend-icon="mdi-fullscreen"
              title="Full screen"
              link
            ></v-list-item>

            <v-list-item
              prepend-icon="mdi-share-variant-outline"
              title="Share screen"
              link
            ></v-list-item>

            <v-divider class="my-2"></v-divider>

            <v-list-item
              prepend-icon="mdi-cog-outline"
              title="Settings"
              link
            ></v-list-item>
          </v-list>
        </v-menu>
      </v-icon-btn>

      <v-icon-btn
        v-model:active="hangup"
        active-variant="outlined"
        base-variant="flat"
        color="error"
        height="48"
        icon="mdi-phone-hangup-outline"
        rounded="xl"
        width="72"
      ></v-icon-btn>
    </v-sheet>
  </v-container>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const caption = shallowRef(false)
  const emoji = shallowRef(false)
  const hangup = shallowRef(false)
  const mic = shallowRef(true)
  const micOptions = shallowRef(false)
  const raised = shallowRef(false)
  const share = shallowRef(false)
  const video = shallowRef(true)
  const videoOptions = shallowRef(false)

  function onClick () {
    console.log('Sharing your screen')
  }
</script>

<script>
  export default {
    data () {
      return {
        caption: false,
        emoji: false,
        raised: false,
        share: false,
        mic: true,
        micOptions: false,
        video: true,
        videoOptions: false,
      }
    },
    methods: {
      onClick () {
        console.log('Sharing your screen')
      },
    },
  }
</script>

```
