# Vuetify component v-autocomplete - usage

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
      <v-autocomplete v-bind="props"></v-autocomplete>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="clear" label="Clearable"></v-checkbox>

      <v-checkbox v-model="chips" label="Chips"></v-checkbox>

      <v-checkbox v-model="multiple" label="Multiple"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-autocomplete'
  const model = ref('default')
  const clear = ref(false)
  const chips = ref(false)
  const multiple = ref(false)
  const options = ['outlined', 'underlined', 'solo', 'solo-filled', 'solo-inverted']
  const props = computed(() => {
    return {
      clearable: clear.value || undefined,
      chips: chips.value || undefined,
      label: 'Autocomplete',
      items: ['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming'],
      multiple: multiple.value || undefined,
      variant: model.value === 'default' ? undefined : model.value,
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

# Vuetify component v-autocomplete - prop filter

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    color="purple-lighten-1"
    max-width="500"
  >
    <v-toolbar color="purple" flat>
      <v-btn icon="mdi-account"></v-btn>

      <v-toolbar-title class="font-weight-light">
        User Profile
      </v-toolbar-title>

      <v-btn
        icon
        @click="isEditing = !isEditing"
      >
        <v-fade-transition leave-absolute>
          <v-icon v-if="isEditing">mdi-close</v-icon>

          <v-icon v-else>mdi-pencil</v-icon>
        </v-fade-transition>
      </v-btn>
    </v-toolbar>

    <v-card-text>
      <v-text-field
        :disabled="!isEditing"
        base-color="white"
        label="Name"
      ></v-text-field>

      <v-autocomplete
        :custom-filter="customFilter"
        :disabled="!isEditing"
        :items="states"
        base-color="white"
        item-title="name"
        item-value="abbr"
        label="State"
      ></v-autocomplete>
    </v-card-text>

    <v-divider></v-divider>

    <v-card-actions>
      <v-spacer></v-spacer>

      <v-btn
        :disabled="!isEditing"
        @click="save"
      >
        Save
      </v-btn>
    </v-card-actions>

    <v-snackbar
      v-model="hasSaved"
      :timeout="2000"
      location="bottom left"
      position="absolute"
      attach
    >
      Your profile has been updated
    </v-snackbar>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const states = [
    { name: 'Florida', abbr: 'FL', id: 1 },
    { name: 'Georgia', abbr: 'GA', id: 2 },
    { name: 'Nebraska', abbr: 'NE', id: 3 },
    { name: 'California', abbr: 'CA', id: 4 },
    { name: 'New York', abbr: 'NY', id: 5 },
  ]

  const hasSaved = ref(false)
  const isEditing = ref(null)

  function customFilter (itemTitle, queryText, item) {
    const textOne = item.raw.name.toLowerCase()
    const textTwo = item.raw.abbr.toLowerCase()
    const searchText = queryText.toLowerCase()
    return textOne.indexOf(searchText) > -1 || textTwo.indexOf(searchText) > -1
  }
  function save () {
    isEditing.value = !isEditing.value
    hasSaved.value = true
  }
</script>

<script>
  export default {
    data: () => ({
      hasSaved: false,
      isEditing: null,
      states: [
        { name: 'Florida', abbr: 'FL', id: 1 },
        { name: 'Georgia', abbr: 'GA', id: 2 },
        { name: 'Nebraska', abbr: 'NE', id: 3 },
        { name: 'California', abbr: 'CA', id: 4 },
        { name: 'New York', abbr: 'NY', id: 5 },
      ],
    }),

    methods: {
      customFilter (itemTitle, queryText, item) {
        const textOne = item.raw.name.toLowerCase()
        const textTwo = item.raw.abbr.toLowerCase()
        const searchText = queryText.toLowerCase()

        return textOne.indexOf(searchText) > -1 ||
          textTwo.indexOf(searchText) > -1
      },
      save () {
        this.isEditing = !this.isEditing
        this.hasSaved = true
      },
    },
  }
</script>

```

# Vuetify component v-autocomplete - misc new tab

Example code

```vue
<template>
  <v-card class="pa-8 d-flex justify-center flex-wrap" theme="dark">
    <v-container class="text-center">
      <v-row justify="center" dense>
        <v-col cols="12">
          <v-img
            class="mx-auto mt-12 mb-16"
            max-height="140"
            max-width="240"
            src="https://cdn.vuetifyjs.com/docs/images/logos/vuetify-logo-dark-text.svg"
          ></v-img>
        </v-col>

        <v-col cols="12">
          <v-autocomplete
            :items="items"
            append-inner-icon="mdi-microphone"
            class="mx-auto"
            density="comfortable"
            menu-icon=""
            placeholder="Search Google or type a URL"
            prepend-inner-icon="mdi-magnify"
            style="max-width: 350px;"
            theme="light"
            variant="solo"
            auto-select-first
            item-props
            rounded
          ></v-autocomplete>
        </v-col>

        <v-col
          v-for="(shortcut, i) in shortcuts"
          :key="i"
          cols="auto"
        >
          <v-card
            :href="shortcut.href"
            class="pa-4"
            rel="noopener noreferrer"
            target="_blank"
            width="112"
            flat
          >
            <v-avatar :icon="shortcut.icon" class="mb-2" color="white" variant="tonal"></v-avatar>

            <div class="text-caption text-truncate" v-text="shortcut.title"></div>
          </v-card>
        </v-col>

        <v-col cols="auto">
          <v-dialog v-model="dialog" max-width="500">
            <template v-slot:activator="{ props }">
              <v-card v-bind="props" class="pa-4" width="112" flat>

                <v-avatar class="mb-2" color="white" icon="mdi-plus" variant="tonal"></v-avatar>

                <div class="text-caption text-truncate">Add shortcut</div>
              </v-card>
            </template>

            <v-card rounded="lg" title="Add shortcut">
              <template v-slot:text>
                <v-label class="text-caption">Name</v-label>

                <v-text-field density="compact" variant="solo-filled" flat></v-text-field>

                <v-label class="text-caption">URL</v-label>

                <v-text-field density="compact" variant="solo-filled" flat></v-text-field>
              </template>

              <div class="py-4 px-5 text-end">
                <v-btn
                  class="text-none me-2"
                  color="blue"
                  text="Cancel"
                  variant="text"
                  border
                  @click="dialog = false"
                ></v-btn>

                <v-btn
                  class="text-none"
                  color="blue"
                  text="Done"
                  variant="flat"
                  @click="dialog = false"
                ></v-btn>
              </div>
            </v-card>
          </v-dialog>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const items = [
    {
      prependIcon: 'mdi-clock-outline',
      title: 'recipe with chicken',
    },
    {
      prependIcon: 'mdi-clock-outline',
      title: 'best hiking trails near me',
    },
    {
      prependIcon: 'mdi-clock-outline',
      title: 'how to learn a new language',
    },
    {
      prependIcon: 'mdi-clock-outline',
      title: 'DIY home organization ideas',
    },
    {
      prependIcon: 'mdi-clock-outline',
      title: 'latest fashion trends',
    },
  ]
  const shortcuts = [
    {
      icon: 'mdi-github',
      title: 'Master ',
      href: 'https://github.com/vuetifyjs/vuetify',
    },
    {
      icon: 'mdi-github',
      title: 'Dev',
      href: 'https://github.com/vuetifyjs/vuetify/tree/dev',
    },
    {
      icon: 'mdi-github',
      title: 'Stable',
      href: 'https://github.com/vuetifyjs/vuetify/tree/v2-stable',
    },
    {
      icon: 'mdi-github',
      title: 'My Pull Requests',
      href: 'https://github.com/vuetifyjs/vuetify/pulls/johnleider',
    },
  ]

  const dialog = ref(false)
</script>

<script>
  export default {
    data: () => ({
      dialog: false,
      items: [
        {
          prependIcon: 'mdi-clock-outline',
          title: 'recipe with chicken',
        },
        {
          prependIcon: 'mdi-clock-outline',
          title: 'best hiking trails near me',
        },
        {
          prependIcon: 'mdi-clock-outline',
          title: 'how to learn a new language',
        },
        {
          prependIcon: 'mdi-clock-outline',
          title: 'DIY home organization ideas',
        },
        {
          prependIcon: 'mdi-clock-outline',
          title: 'latest fashion trends',
        },
      ],
      shortcuts: [
        {
          icon: 'mdi-github',
          title: 'Master ',
          href: 'https://github.com/vuetifyjs/vuetify',
        },
        {
          icon: 'mdi-github',
          title: 'Dev',
          href: 'https://github.com/vuetifyjs/vuetify/tree/dev',
        },
        {
          icon: 'mdi-github',
          title: 'Stable',
          href: 'https://github.com/vuetifyjs/vuetify/tree/v2-stable',
        },
        {
          icon: 'mdi-github',
          title: 'My Pull Requests',
          href: 'https://github.com/vuetifyjs/vuetify/pulls/johnleider',
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-autocomplete - prop density

Example code

```vue
<template>
  <v-card>
    <v-container fluid>
      <v-row>
        <v-col cols="12">
          <v-autocomplete
            v-model="values"
            :items="items"
            label="Default"
          ></v-autocomplete>
        </v-col>

        <v-col cols="12">
          <v-autocomplete
            v-model="values"
            :items="items"
            density="comfortable"
            label="Comfortable"
          ></v-autocomplete>
        </v-col>

        <v-col cols="12">
          <v-autocomplete
            v-model="values"
            :items="items"
            density="compact"
            label="Compact"
          ></v-autocomplete>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ['foo', 'bar', 'fizz', 'buzz']

  const values = ref('foo')
</script>

<script>
  export default {
    data: () => ({
      items: ['foo', 'bar', 'fizz', 'buzz'],
      values: 'foo',
    }),
  }
</script>

```

# Vuetify component v-autocomplete - misc asynchronous items

Example code

```vue
<template>
  <v-toolbar color="teal">
    <v-toolbar-title>State selection</v-toolbar-title>

    <v-autocomplete
      v-model="select"
      v-model:search="search"
      :items="items"
      :loading="loading"
      class="mx-4"
      density="comfortable"
      label="What state are you from?"
      style="max-width: 300px;"
      hide-details
      hide-no-data
    ></v-autocomplete>

    <v-btn icon="mdi-dots-vertical"></v-btn>
  </v-toolbar>
</template>

<script setup>
  import { ref, watch } from 'vue'

  const states = [
    'Alabama',
    'Alaska',
    'American Samoa',
    'Arizona',
    'Arkansas',
    'California',
    'Colorado',
    'Connecticut',
    'Delaware',
    'District of Columbia',
    'Federated States of Micronesia',
    'Florida',
    'Georgia',
    'Guam',
    'Hawaii',
    'Idaho',
    'Illinois',
    'Indiana',
    'Iowa',
    'Kansas',
    'Kentucky',
    'Louisiana',
    'Maine',
    'Marshall Islands',
    'Maryland',
    'Massachusetts',
    'Michigan',
    'Minnesota',
    'Mississippi',
    'Missouri',
    'Montana',
    'Nebraska',
    'Nevada',
    'New Hampshire',
    'New Jersey',
    'New Mexico',
    'New York',
    'North Carolina',
    'North Dakota',
    'Northern Mariana Islands',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Palau',
    'Pennsylvania',
    'Puerto Rico',
    'Rhode Island',
    'South Carolina',
    'South Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Vermont',
    'Virgin Island',
    'Virginia',
    'Washington',
    'West Virginia',
    'Wisconsin',
    'Wyoming',
  ]

  const loading = ref(false)
  const items = ref([])
  const search = ref(null)
  const select = ref(null)

  watch(search, val => {
    val && val !== select.value && querySelections(val)
  })

  function querySelections (v) {
    loading.value = true
    setTimeout(() => {
      items.value = states.filter(e => {
        return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
      })
      loading.value = false
    }, 500)
  }
</script>

<script>
  export default {
    data () {
      return {
        loading: false,
        items: [],
        search: null,
        select: null,
        states: [
          'Alabama',
          'Alaska',
          'American Samoa',
          'Arizona',
          'Arkansas',
          'California',
          'Colorado',
          'Connecticut',
          'Delaware',
          'District of Columbia',
          'Federated States of Micronesia',
          'Florida',
          'Georgia',
          'Guam',
          'Hawaii',
          'Idaho',
          'Illinois',
          'Indiana',
          'Iowa',
          'Kansas',
          'Kentucky',
          'Louisiana',
          'Maine',
          'Marshall Islands',
          'Maryland',
          'Massachusetts',
          'Michigan',
          'Minnesota',
          'Mississippi',
          'Missouri',
          'Montana',
          'Nebraska',
          'Nevada',
          'New Hampshire',
          'New Jersey',
          'New Mexico',
          'New York',
          'North Carolina',
          'North Dakota',
          'Northern Mariana Islands',
          'Ohio',
          'Oklahoma',
          'Oregon',
          'Palau',
          'Pennsylvania',
          'Puerto Rico',
          'Rhode Island',
          'South Carolina',
          'South Dakota',
          'Tennessee',
          'Texas',
          'Utah',
          'Vermont',
          'Virgin Island',
          'Virginia',
          'Washington',
          'West Virginia',
          'Wisconsin',
          'Wyoming',
        ],
      }
    },
    watch: {
      search (val) {
        val && val !== this.select && this.querySelections(val)
      },
    },
    methods: {
      querySelections (v) {
        this.loading = true
        // Simulated ajax query
        setTimeout(() => {
          this.items = this.states.filter(e => {
            return (e || '').toLowerCase().indexOf((v || '').toLowerCase()) > -1
          })
          this.loading = false
        }, 500)
      },
    },
  }
</script>

```

# Vuetify component v-autocomplete - slot item and selection

Example code

```vue
<template>
  <v-card
    :loading="isUpdating"
    class="mx-auto"
    color="blue-grey-darken-1"
    max-width="420"
  >
    <template v-slot:loader="{ isActive }">
      <v-progress-linear
        :active="isActive"
        color="green-lighten-3"
        height="4"
        indeterminate
      ></v-progress-linear>
    </template>

    <v-img
      height="200"
      src="https://cdn.vuetifyjs.com/images/cards/dark-beach.jpg"
      cover
    >
      <v-row class="pa-3">
        <v-col cols="12">
          <v-menu
            location="bottom start"
            origin="overlap"
            transition="slide-y-transition"
          >
            <template v-slot:activator="{ props }">
              <v-btn
                v-bind="props"
                density="comfortable"
                icon="mdi-dots-vertical"
                variant="tonal"
              ></v-btn>
            </template>

            <v-list :lines="false">
              <v-list-item
                title="Update"
                @click="isUpdating = true"
              ></v-list-item>
            </v-list>
          </v-menu>
        </v-col>

        <v-row>
          <v-col class="text-center">
            <h3 class="text-h5">{{ name }}</h3>

            <span class="text-grey-lighten-1">{{ title }}</span>
          </v-col>
        </v-row>
      </v-row>
    </v-img>

    <v-form>
      <v-container>
        <v-row dense>
          <v-col cols="12" md="6">
            <v-text-field
              v-model="name"
              :disabled="isUpdating"
              color="blue-grey-lighten-2"
              label="Name"
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="6">
            <v-text-field
              v-model="title"
              :disabled="isUpdating"
              color="blue-grey-lighten-2"
              label="Title"
            ></v-text-field>
          </v-col>

          <v-col cols="12">
            <v-autocomplete
              v-model="friends"
              :disabled="isUpdating"
              :items="people"
              color="blue-grey-lighten-2"
              item-title="name"
              item-value="name"
              label="Select"
              chips
              closable-chips
              multiple
            >
              <template v-slot:chip="{ props, item }">
                <v-chip
                  v-bind="props"
                  :prepend-avatar="item.raw.avatar"
                  :text="item.raw.name"
                ></v-chip>
              </template>

              <template v-slot:item="{ props, item }">
                <v-list-item
                  v-bind="props"
                  :prepend-avatar="item.raw.avatar"
                  :subtitle="item.raw.group"
                  :title="item.raw.name"
                ></v-list-item>
              </template>
            </v-autocomplete>
          </v-col>
        </v-row>
      </v-container>
    </v-form>

    <v-divider></v-divider>

    <v-card-actions>
      <v-switch
        v-model="autoUpdate"
        :disabled="isUpdating"
        class="mt-0 ms-2"
        color="green-lighten-2"
        density="compact"
        label="Auto Update"
        hide-details
      ></v-switch>

      <v-spacer></v-spacer>

      <v-btn
        :disabled="autoUpdate"
        :loading="isUpdating"
        :variant="isUpdating ? 'tonal' : undefined"
        color="blue-grey-lighten-3"
        prepend-icon="mdi-update"
        @click="isUpdating = true"
      >
        Update Now
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
  import { ref, watch } from 'vue'

  const srcs = {
    1: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
    2: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
    3: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
    4: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
    5: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
  }
  const people = [
    { name: 'Sandra Adams', group: 'Group 1', avatar: srcs[1] },
    { name: 'Ali Connors', group: 'Group 1', avatar: srcs[2] },
    { name: 'Trevor Hansen', group: 'Group 1', avatar: srcs[3] },
    { name: 'Tucker Smith', group: 'Group 1', avatar: srcs[2] },
    { name: 'Britta Holt', group: 'Group 2', avatar: srcs[4] },
    { name: 'Jane Smith ', group: 'Group 2', avatar: srcs[5] },
    { name: 'John Smith', group: 'Group 2', avatar: srcs[1] },
    { name: 'Sandra Williams', group: 'Group 2', avatar: srcs[3] },
  ]

  const autoUpdate = ref(true)
  const friends = ref(['Sandra Adams', 'Britta Holt'])
  const isUpdating = ref(false)
  const name = ref('Midnight Crew')
  const title = ref('The summer breeze')

  let timeout = -1
  watch(isUpdating, val => {
    clearTimeout(timeout)
    if (val) {
      timeout = setTimeout(() => (isUpdating.value = false), 3000)
    }
  })
</script>

<script>
  export default {
    data () {
      const srcs = {
        1: 'https://cdn.vuetifyjs.com/images/lists/1.jpg',
        2: 'https://cdn.vuetifyjs.com/images/lists/2.jpg',
        3: 'https://cdn.vuetifyjs.com/images/lists/3.jpg',
        4: 'https://cdn.vuetifyjs.com/images/lists/4.jpg',
        5: 'https://cdn.vuetifyjs.com/images/lists/5.jpg',
      }

      return {
        autoUpdate: true,
        friends: ['Sandra Adams', 'Britta Holt'],
        isUpdating: false,
        name: 'Midnight Crew',
        people: [
          // TODO: https://github.com/vuetifyjs/vuetify/issues/15721
          // { header: 'Group 1' },
          { name: 'Sandra Adams', group: 'Group 1', avatar: srcs[1] },
          { name: 'Ali Connors', group: 'Group 1', avatar: srcs[2] },
          { name: 'Trevor Hansen', group: 'Group 1', avatar: srcs[3] },
          { name: 'Tucker Smith', group: 'Group 1', avatar: srcs[2] },
          // { divider: true },
          // { header: 'Group 2' },
          { name: 'Britta Holt', group: 'Group 2', avatar: srcs[4] },
          { name: 'Jane Smith ', group: 'Group 2', avatar: srcs[5] },
          { name: 'John Smith', group: 'Group 2', avatar: srcs[1] },
          { name: 'Sandra Williams', group: 'Group 2', avatar: srcs[3] },
        ],
        title: 'The summer breeze',
        timeout: null,
      }
    },

    watch: {
      isUpdating (val) {
        clearTimeout(this.timeout)

        if (val) {
          this.timeout = setTimeout(() => (this.isUpdating = false), 3000)
        }
      },
    },

    methods: {
      remove (item) {
        const index = this.friends.indexOf(item.name)
        if (index >= 0) this.friends.splice(index, 1)
      },
    },
  }
</script>

```

# Vuetify component v-autocomplete - misc state selector

Example code

```vue
<template>
  <v-card>
    <v-card-title class="text-h5 font-weight-regular bg-blue-grey">
      Profile
    </v-card-title>

    <v-card-text>
      <div class="text-caption pa-3">Where do you live?</div>

      <v-autocomplete
        v-model="model"
        :hint="!isEditing ? 'Click the icon to edit' : 'Click the icon to save'"
        :items="states"
        :label="`State — ${isEditing ? 'Editable' : 'Readonly'}`"
        :readonly="!isEditing"
        prepend-icon="mdi-city"
        persistent-hint
      >
        <template v-slot:append>
          <v-slide-x-reverse-transition mode="out-in">
            <v-icon
              :key="`icon-${isEditing}`"
              :color="isEditing ? 'success' : 'info'"
              :icon="isEditing ? 'mdi-check-outline' : 'mdi-circle-edit-outline'"
              @click="isEditing = !isEditing"
            ></v-icon>
          </v-slide-x-reverse-transition>
        </template>
      </v-autocomplete>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const isEditing = ref(false)
  const model = ref(null)

  const states = [
    'Alabama',
    'Alaska',
    'American Samoa',
    'Arizona',
    'Arkansas',
    'California',
    'Colorado',
    'Connecticut',
    'Delaware',
    'District of Columbia',
    'Federated States of Micronesia',
    'Florida',
    'Georgia',
    'Guam',
    'Hawaii',
    'Idaho',
    'Illinois',
    'Indiana',
    'Iowa',
    'Kansas',
    'Kentucky',
    'Louisiana',
    'Maine',
    'Marshall Islands',
    'Maryland',
    'Massachusetts',
    'Michigan',
    'Minnesota',
    'Mississippi',
    'Missouri',
    'Montana',
    'Nebraska',
    'Nevada',
    'New Hampshire',
    'New Jersey',
    'New Mexico',
    'New York',
    'North Carolina',
    'North Dakota',
    'Northern Mariana Islands',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Palau',
    'Pennsylvania',
    'Puerto Rico',
    'Rhode Island',
    'South Carolina',
    'South Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Vermont',
    'Virgin Island',
    'Virginia',
    'Washington',
    'West Virginia',
    'Wisconsin',
    'Wyoming',
  ]
</script>

<script>
  export default {
    data () {
      return {
        isEditing: false,
        model: null,
        states: [
          'Alabama', 'Alaska', 'American Samoa', 'Arizona',
          'Arkansas', 'California', 'Colorado', 'Connecticut',
          'Delaware', 'District of Columbia', 'Federated States of Micronesia',
          'Florida', 'Georgia', 'Guam', 'Hawaii', 'Idaho',
          'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
          'Louisiana', 'Maine', 'Marshall Islands', 'Maryland',
          'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
          'Missouri', 'Montana', 'Nebraska', 'Nevada',
          'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
          'North Carolina', 'North Dakota', 'Northern Mariana Islands', 'Ohio',
          'Oklahoma', 'Oregon', 'Palau', 'Pennsylvania', 'Puerto Rico',
          'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee',
          'Texas', 'Utah', 'Vermont', 'Virgin Island', 'Virginia',
          'Washington', 'West Virginia', 'Wisconsin', 'Wyoming',
        ],
      }
    },
  }
</script>

```
