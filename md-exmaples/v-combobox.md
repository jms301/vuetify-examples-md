# Vuetify component v-combobox - usage

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
      <v-combobox v-bind="props"></v-combobox>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="clear" label="Clearable"></v-checkbox>

      <v-checkbox v-model="chips" label="Chips"></v-checkbox>

      <v-checkbox v-model="multiple" label="Multiple"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-combobox'
  const model = ref('default')
  const clear = ref(false)
  const chips = ref(false)
  const multiple = ref(false)
  const options = ['outlined', 'underlined', 'solo', 'solo-filled', 'solo-inverted']
  const props = computed(() => {
    return {
      clearable: clear.value || undefined,
      chips: chips.value || undefined,
      multiple: multiple.value || undefined,
      label: 'Combobox',
      items: ['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming'],
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

# Vuetify component v-combobox - prop density

Example code

```vue
<template>
  <v-card>
    <v-container fluid>
      <v-row>
        <v-col cols="12">
          <v-combobox
            v-model="value"
            :items="items"
            label="Default"
          ></v-combobox>
        </v-col>
        <v-col cols="12">
          <v-combobox
            v-model="value"
            :items="items"
            density="comfortable"
            label="Comfortable"
          ></v-combobox>
        </v-col>
        <v-col cols="12">
          <v-combobox
            v-model="value"
            :items="items"
            density="compact"
            label="Compact"
          ></v-combobox>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const items = ['foo', 'bar', 'fizz', 'buzz']

  const value = ref('foo')
</script>

<script>
  export default {
    data: () => ({
      items: ['foo', 'bar', 'fizz', 'buzz'],
      value: 'foo',
    }),
  }
</script>

```

# Vuetify component v-combobox - prop multiple

Example code

```vue
<template>
  <v-container fluid>
    <v-row>
      <v-col cols="12">
        <v-combobox
          v-model="select"
          :items="items"
          label="Select a favorite activity or create a new one"
          multiple
        ></v-combobox>
      </v-col>
      <v-col cols="12">
        <v-combobox
          v-model="select"
          :items="items"
          label="I use chips"
          chips
          multiple
        ></v-combobox>
      </v-col>
      <v-col cols="12">
        <v-combobox
          v-model="select"
          :items="items"
          label="I use a scoped slot"
          multiple
        >
          <template v-slot:selection="data">
            <v-chip
              :key="JSON.stringify(data.item)"
              v-bind="data.attrs"
              :disabled="data.disabled"
              :model-value="data.selected"
              size="small"
              @click:close="data.parent.selectItem(data.item)"
            >
              <template v-slot:prepend>
                <v-avatar
                  class="bg-accent text-uppercase"
                  start
                >{{ data.item.title.slice(0, 1) }}</v-avatar>
              </template>
              {{ data.item.title }}
            </v-chip>
          </template>
        </v-combobox>
      </v-col>
      <v-col cols="12">
        <v-combobox
          v-model="select"
          label="I'm readonly"
          chips
          multiple
          readonly
        ></v-combobox>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
  import { ref } from 'vue'

  const select = ref(['Vuetify', 'Programming'])

  const items = [
    'Programming',
    'Design',
    'Vue',
    'Vuetify',
  ]
</script>

<script>
  export default {
    data () {
      return {
        select: ['Vuetify', 'Programming'],
        items: [
          'Programming',
          'Design',
          'Vue',
          'Vuetify',
        ],
      }
    },
  }
</script>

```

# Vuetify component v-combobox - slot no data

Example code

```vue
<template>
  <v-container fluid>
    <v-combobox
      v-model="model"
      v-model:search="search"
      :hide-no-data="false"
      :items="items"
      hint="Maximum of 5 tags"
      label="Add some tags"
      chips
      hide-selected
      multiple
      persistent-hint
    >
      <template v-slot:no-data>
        <v-list-item>
          <v-list-item-title>
            No results matching "<strong>{{ search }}</strong>". Press <kbd>enter</kbd> to create a new one
          </v-list-item-title>
        </v-list-item>
      </template>
    </v-combobox>
  </v-container>
</template>

<script setup>
  import { nextTick, ref, watch } from 'vue'

  const items = ['Gaming', 'Programming', 'Vue', 'Vuetify']

  const model = ref(['Vuetify'])
  const search = ref(null)

  watch(model, val => {
    if (val.length > 5) {
      nextTick(() => model.value.pop())
    }
  })
</script>

<script>
  export default {
    data: () => ({
      items: ['Gaming', 'Programming', 'Vue', 'Vuetify'],
      model: ['Vuetify'],
      search: null,
    }),

    watch: {
      model (val) {
        if (val.length > 5) {
          this.$nextTick(() => this.model.pop())
        }
      },
    },
  }
</script>

```

# Vuetify component v-combobox - misc advanced

Example code

```vue
<template>
  <v-container fluid>
    <v-combobox
      v-model="model"
      v-model:search="search"
      :custom-filter="filter"
      :items="items"
      label="Search for an option"
      variant="solo"
      hide-selected
      multiple
    >
      <template v-slot:selection="{ item, index }">
        <v-chip
          v-if="item === Object(item)"
          :color="`${item.raw.color}-lighten-3`"
          :text="item.title"
          size="small"
          variant="flat"
          closable
          label
          @click:close="removeSelection(index)"
        ></v-chip>
      </template>
      <template v-slot:item="{ props, item }">
        <v-list-item v-if="item.raw.header && search">
          <span class="mr-3">Create</span>
          <v-chip
            :color="`${colors[nonce - 1]}-lighten-3`"
            size="small"
            variant="flat"
            label
          >
            {{ search }}
          </v-chip>
        </v-list-item>
        <v-list-subheader v-else-if="item.raw.header" :title="item.title"></v-list-subheader>
        <v-list-item v-else @click="props.onClick">
          <v-text-field
            v-if="editingItem === item.raw"
            v-model="editingItem.title"
            bg-color="transparent"
            class="mr-3"
            density="compact"
            variant="plain"
            autofocus
            hide-details
            @click.stop
            @keydown.stop
            @keyup.enter="edit(item.raw)"
          ></v-text-field>
          <v-chip
            v-else
            :color="`${item.raw.color}-lighten-3`"
            :text="item.raw.title"
            variant="flat"
            label
          ></v-chip>
          <template v-slot:append>
            <v-btn
              :color="editingItem !== item.raw ? 'primary' : 'success'"
              :icon="editingItem !== item.raw ? 'mdi-pencil' : 'mdi-check'"
              size="small"
              variant="text"
              @click.stop.prevent="edit(item.raw)"
            ></v-btn>
          </template>
        </v-list-item>
      </template>
    </v-combobox>
  </v-container>
</template>

<script setup>
  import { onMounted, ref, watch } from 'vue'

  const colors = ['green', 'purple', 'indigo', 'cyan', 'teal', 'orange']
  const editingItem = ref(null)
  const items = ref([
    { header: true, title: 'Select an option or create one' },
    { title: 'Foo', color: 'blue' },
    { title: 'Bar', color: 'red' },
  ])
  const nonce = ref(1)
  const model = ref([])
  const search = ref(null)

  onMounted(() => {
    model.value.push(items.value[1])
  })

  watch(model, (val, prev) => {
    if (val.length === prev.length) return

    model.value = val.map(v => {
      if (typeof v === 'string') {
        v = {
          title: v,
          color: colors[nonce.value - 1],
        }

        items.value.push(v)

        nonce.value++
      }

      return v
    })
  })

  function edit (item) {
    if (!editingItem.value) {
      editingItem.value = item
    } else {
      editingItem.value = null
    }
  }

  function filter (value, queryText, item) {
    const toLowerCaseString = val =>
      String(val != null ? val : '').toLowerCase()

    const query = toLowerCaseString(queryText)

    const availableOptions = items.value.filter(x => !model.value.includes(x))
    const hasAnyMatch = availableOptions.some(
      x => !x.header && toLowerCaseString(x.title).includes(query)
    )
    if (item.raw.header) return !hasAnyMatch

    const text = toLowerCaseString(item.raw.title)

    return text.includes(query)
  }

  function removeSelection (index) {
    model.value.splice(index, 1)
  }
</script>

<script>
  export default {
    data: () => ({
      colors: ['green', 'purple', 'indigo', 'cyan', 'teal', 'orange'],
      editingItem: null,
      items: [
        { header: true, title: 'Select an option or create one' },
        {
          title: 'Foo',
          color: 'blue',
        },
        {
          title: 'Bar',
          color: 'red',
        },
      ],
      nonce: 1,
      model: [],
      search: null,
    }),

    watch: {
      model (val, prev) {
        if (val.length === prev.length) return

        this.model = val.map(v => {
          if (typeof v === 'string') {
            v = {
              title: v,
              color: this.colors[this.nonce - 1],
            }

            this.items.push(v)

            this.nonce++
          }

          return v
        })
      },
    },

    mounted () {
      this.model = [this.items[1]]
    },

    methods: {
      edit (item) {
        if (!this.editingItem) {
          this.editingItem = item
        } else {
          this.editingItem = null
        }
      },
      filter (value, queryText, item) {
        const toLowerCaseString = val =>
          String(val != null ? val : '').toLowerCase()

        const query = toLowerCaseString(queryText)

        const availableOptions = this.items.filter(x => !this.model.includes(x))
        const hasAnyMatch = availableOptions.some(
          x => !x.header && toLowerCaseString(x.title).includes(query)
        )
        if (item.raw.header) return !hasAnyMatch

        const text = toLowerCaseString(item.raw.title)

        return text.includes(query)
      },
      removeSelection (index) {
        this.model.splice(index, 1)
      },
    },
  }
</script>

```
