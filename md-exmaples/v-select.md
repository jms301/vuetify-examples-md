# Vuetify component v-select - usage

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
      <v-select v-bind="props"></v-select>
    </div>

    <template v-slot:configuration>
      <v-checkbox v-model="clear" label="Clearable"></v-checkbox>

      <v-checkbox v-model="chips" label="Chips"></v-checkbox>

      <v-checkbox v-model="multiple" label="Multiple"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-select'
  const model = shallowRef('default')
  const clear = shallowRef(false)
  const chips = shallowRef(false)
  const multiple = shallowRef(false)
  const options = ['outlined', 'underlined', 'solo', 'solo-filled', 'solo-inverted']
  const props = computed(() => {
    return {
      clearable: clear.value || undefined,
      chips: chips.value || undefined,
      label: 'Select',
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

# Vuetify component v-select - prop dense

Example code

```vue
<template>
  <v-select
    :items="items"
    density="compact"
    label="Compact"
  ></v-select>

  <v-select
    :items="items"
    density="comfortable"
    label="Comfortable"
  ></v-select>

  <v-select
    :items="items"
    label="Default"
  ></v-select>
</template>

<script setup>
  const items = ['Foo', 'Bar', 'Fizz', 'Buzz']
</script>

<script>
  export default {
    data: () => ({
      items: ['Foo', 'Bar', 'Fizz', 'Buzz'],
    }),
  }
</script>

```

# Vuetify component v-select - prop multiple

Example code

```vue
<template>
  <v-select
    v-model="favorites"
    :items="states"
    hint="Pick your favorite states"
    label="Select"
    multiple
    persistent-hint
  ></v-select>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const favorites = shallowRef([])

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
        favorites: [],
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

# Vuetify component v-select - slot selection

Example code

```vue
<template>
  <v-select
    v-model="value"
    :items="items"
    label="Select Item"
    multiple
  >
    <template v-slot:selection="{ item, index }">
      <v-chip v-if="index < 2" :text="item.title"></v-chip>

      <span
        v-if="index === 2"
        class="text-grey text-caption align-self-center"
      >
        (+{{ value.length - 2 }} others)
      </span>
    </template>
  </v-select>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const value = shallowRef(['foo', 'bar', 'fizz'])
  const items = ['foo', 'bar', 'fizz', 'buzz', 'fizzbuzz', 'foobar']
</script>

<script>
  export default {
    data: () => ({
      value: ['foo', 'bar', 'fizz'],
      items: ['foo', 'bar', 'fizz', 'buzz', 'fizzbuzz', 'foobar'],
    }),
  }
</script>

```

# Vuetify component v-select - prop menu props

Example code

```vue
<template>
  <v-select
    :items="items"
    :menu-props="{ scrim: true, scrollStrategy: 'close' }"
    label="Label"
  ></v-select>
</template>

<script setup>
  const items = ['Foo', 'Bar', 'Fizz', 'Buzz']
</script>

<script>
  export default {
    data: () => ({
      items: ['Foo', 'Bar', 'Fizz', 'Buzz'],
    }),
  }
</script>

```

# Vuetify component v-select - prop custom title and value

Example code

```vue
<template>
  <v-select
    v-model="select"
    :hint="`${select.state}, ${select.abbr}`"
    :items="items"
    item-title="state"
    item-value="abbr"
    label="Select"
    persistent-hint
    return-object
    single-line
  ></v-select>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const select = shallowRef({ state: 'Florida', abbr: 'FL' })

  const items = [
    { state: 'Florida', abbr: 'FL' },
    { state: 'Georgia', abbr: 'GA' },
    { state: 'Nebraska', abbr: 'NE' },
    { state: 'California', abbr: 'CA' },
    { state: 'New York', abbr: 'NY' },
  ]
</script>

<script>
  export default {
    data () {
      return {
        select: { state: 'Florida', abbr: 'FL' },
        items: [
          { state: 'Florida', abbr: 'FL' },
          { state: 'Georgia', abbr: 'GA' },
          { state: 'Nebraska', abbr: 'NE' },
          { state: 'California', abbr: 'CA' },
          { state: 'New York', abbr: 'NY' },
        ],
      }
    },
  }
</script>

```

# Vuetify component v-select - prop readonly

Example code

```vue
<template>
  <v-select
    v-model="model"
    :items="items"
    label="Read-only"
    readonly
  ></v-select>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const model = shallowRef('Foo')
  const items = ['Foo', 'Bar', 'Fizz', 'Buzz']
</script>

<script>
  export default {
    data: () => ({
      items: ['Foo', 'Bar', 'Fizz', 'Buzz'],
      model: 'Foo',
    }),
  }
</script>

```

# Vuetify component v-select - prop item props

Example code

```vue
<template>
  <v-select
    :item-props="itemProps"
    :items="items"
    label="User"
  ></v-select>
</template>

<script setup>
  const items = [
    {
      name: 'John',
      department: 'Marketing',
    },
    {
      name: 'Jane',
      department: 'Engineering',
    },
    {
      name: 'Joe',
      department: 'Sales',
    },
    {
      name: 'Janet',
      department: 'Engineering',
    },
    {
      name: 'Jake',
      department: 'Marketing',
    },
    {
      name: 'Jack',
      department: 'Sales',
    },
  ]

  function itemProps (item) {
    return {
      title: item.name,
      subtitle: item.department,
    }
  }
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          name: 'John',
          department: 'Marketing',
        },
        {
          name: 'Jane',
          department: 'Engineering',
        },
        {
          name: 'Joe',
          department: 'Sales',
        },
        {
          name: 'Janet',
          department: 'Engineering',
        },
        {
          name: 'Jake',
          department: 'Marketing',
        },
        {
          name: 'Jack',
          department: 'Sales',
        },
      ],
    }),

    methods: {
      itemProps (item) {
        return {
          title: item.name,
          subtitle: item.department,
        }
      },
    },
  }
</script>

```

# Vuetify component v-select - prop disabled

Example code

```vue
<template>
  <v-select
    :items="items"
    label="Disabled"
    disabled
  ></v-select>
</template>

<script setup>
  const items = ['Foo', 'Bar', 'Fizz', 'Buzz']
</script>

<script>
  export default {
    data: () => ({
      items: ['Foo', 'Bar', 'Fizz', 'Buzz'],
    }),
  }
</script>

```

# Vuetify component v-select - slot item

Example code

```vue
<template>
  <v-select :items="items" item-title="name" label="User">
    <template v-slot:item="{ props: itemProps, item }">
      <v-list-item v-bind="itemProps" :subtitle="item.raw.department"></v-list-item>
    </template>
  </v-select>
</template>

<script setup>
  const items = [
    {
      name: 'John',
      department: 'Marketing',
    },
    {
      name: 'Jane',
      department: 'Engineering',
    },
    {
      name: 'Joe',
      department: 'Sales',
    },
    {
      name: 'Janet',
      department: 'Engineering',
    },
    {
      name: 'Jake',
      department: 'Marketing',
    },
    {
      name: 'Jack',
      department: 'Sales',
    },
  ]
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          name: 'John',
          department: 'Marketing',
        },
        {
          name: 'Jane',
          department: 'Engineering',
        },
        {
          name: 'Joe',
          department: 'Sales',
        },
        {
          name: 'Janet',
          department: 'Engineering',
        },
        {
          name: 'Jake',
          department: 'Marketing',
        },
        {
          name: 'Jack',
          department: 'Sales',
        },
      ],
    }),
  }
</script>

```

# Vuetify component v-select - prop chips

Example code

```vue
<template>
  <v-select
    v-model="value"
    :items="items"
    label="Chips"
    chips
    multiple
  ></v-select>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const items = shallowRef(['foo', 'bar', 'fizz', 'buzz'])
  const value = shallowRef(['foo', 'bar', 'fizz', 'buzz'])
</script>

<script>
  export default {
    data: () => ({
      items: ['foo', 'bar', 'fizz', 'buzz'],
      value: ['foo', 'bar', 'fizz', 'buzz'],
    }),
  }
</script>

```

# Vuetify component v-select - slot append and prepend item

Example code

```vue
<template>
  <v-select
    v-model="selectedFruits"
    :items="fruits"
    label="Favorite Fruits"
    multiple
  >
    <template v-slot:prepend-item>
      <v-list-item
        title="Select All"
        @click="toggle"
      >
        <template v-slot:prepend>
          <v-checkbox-btn
            :color="likesSomeFruit ? 'indigo-darken-4' : undefined"
            :indeterminate="likesSomeFruit && !likesAllFruit"
            :model-value="likesAllFruit"
          ></v-checkbox-btn>
        </template>
      </v-list-item>

      <v-divider class="mt-2"></v-divider>
    </template>

    <template v-slot:append-item>
      <v-divider class="mb-2"></v-divider>

      <v-list-item
        :subtitle="subtitle"
        :title="title"
        disabled
      >
        <template v-slot:prepend>
          <v-avatar color="primary" icon="mdi-food-apple"></v-avatar>
        </template>
      </v-list-item>
    </template>
  </v-select>
</template>

<script setup>
  import { computed, shallowRef } from 'vue'

  const fruits = [
    'Apples',
    'Apricots',
    'Avocado',
    'Bananas',
    'Blueberries',
    'Blackberries',
    'Boysenberries',
    'Bread fruit',
    'Cantaloupes (cantalope)',
    'Cherries',
    'Cranberries',
    'Cucumbers',
    'Currants',
    'Dates',
    'Eggplant',
    'Figs',
    'Grapes',
    'Grapefruit',
    'Guava',
    'Honeydew melons',
    'Huckleberries',
    'Kiwis',
    'Kumquat',
    'Lemons',
    'Limes',
    'Mangos',
    'Mulberries',
    'Muskmelon',
    'Nectarines',
    'Olives',
    'Oranges',
    'Papaya',
    'Peaches',
    'Pears',
    'Persimmon',
    'Pineapple',
    'Plums',
    'Pomegranate',
    'Raspberries',
    'Rose Apple',
    'Starfruit',
    'Strawberries',
    'Tangerines',
    'Tomatoes',
    'Watermelons',
    'Zucchini',
  ]

  const selectedFruits = shallowRef([])

  const likesAllFruit = computed(() => {
    return selectedFruits.value.length === fruits.length
  })
  const likesSomeFruit = computed(() => {
    return selectedFruits.value.length > 0
  })
  const title = computed(() => {
    if (likesAllFruit.value) return 'Holy smokes, someone call the fruit police!'
    if (likesSomeFruit.value) return 'Fruit Count'
    return 'How could you not like fruit?'
  })
  const subtitle = computed(() => {
    if (likesAllFruit.value) return undefined
    if (likesSomeFruit.value) return selectedFruits.value.length
    return 'Go ahead, make a selection above!'
  })

  function toggle () {
    if (likesAllFruit.value) {
      selectedFruits.value = []
    } else {
      selectedFruits.value = fruits.slice()
    }
  }
</script>

<script>
  export default {
    data: () => ({
      fruits: [
        'Apples',
        'Apricots',
        'Avocado',
        'Bananas',
        'Blueberries',
        'Blackberries',
        'Boysenberries',
        'Bread fruit',
        'Cantaloupes (cantalope)',
        'Cherries',
        'Cranberries',
        'Cucumbers',
        'Currants',
        'Dates',
        'Eggplant',
        'Figs',
        'Grapes',
        'Grapefruit',
        'Guava',
        'Honeydew melons',
        'Huckleberries',
        'Kiwis',
        'Kumquat',
        'Lemons',
        'Limes',
        'Mangos',
        'Mulberries',
        'Muskmelon',
        'Nectarines',
        'Olives',
        'Oranges',
        'Papaya',
        'Peaches',
        'Pears',
        'Persimmon',
        'Pineapple',
        'Plums',
        'Pomegranate',
        'Raspberries',
        'Rose Apple',
        'Starfruit',
        'Strawberries',
        'Tangerines',
        'Tomatoes',
        'Watermelons',
        'Zucchini',
      ],
      selectedFruits: [],
    }),

    computed: {
      likesAllFruit () {
        return this.selectedFruits.length === this.fruits.length
      },
      likesSomeFruit () {
        return this.selectedFruits.length > 0
      },
      title () {
        if (this.likesAllFruit) return 'Holy smokes, someone call the fruit police!'

        if (this.likesSomeFruit) return 'Fruit Count'

        return 'How could you not like fruit?'
      },
      subtitle () {
        if (this.likesAllFruit) return undefined

        if (this.likesSomeFruit) return this.selectedFruits.length

        return 'Go ahead, make a selection above!'
      },
    },

    methods: {
      toggle () {
        if (this.likesAllFruit) {
          this.selectedFruits = []
        } else {
          this.selectedFruits = this.fruits.slice()
        }
      },
    },
  }
</script>

```
