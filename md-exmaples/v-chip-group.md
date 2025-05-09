# Vuetify component v-chip-group - usage

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
      <v-chip-group v-bind="props">
        <v-chip>Chip 1</v-chip>

        <v-chip>Chip 2</v-chip>

        <v-chip>Chip 3</v-chip>
      </v-chip-group>
    </div>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-chip-group'
  const model = ref('default')
  const options = ['filter']
  const props = computed(() => {
    return {
      filter: model.value === 'filter' || undefined,
    }
  })

  const slots = computed(() => {
    return `
  <v-chip>Chip 1</v-chip>

  <v-chip>Chip 2</v-chip>

  <v-chip>Chip 3</v-chip>
`
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-chip-group - prop filter

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-toolbar color="deep-purple-accent-4">
      <v-btn icon="mdi-close"></v-btn>

      <v-toolbar-title>Filter results</v-toolbar-title>
    </v-toolbar>

    <v-card-text>
      <h2 class="text-h6 mb-2">Choose amenities</h2>

      <v-chip-group
        v-model="amenities"
        column
        multiple
      >
        <v-chip
          text="Elevator"
          variant="outlined"
          filter
        ></v-chip>

        <v-chip
          text="Washer / Dryer"
          variant="outlined"
          filter
        ></v-chip>

        <v-chip
          text="Fireplace"
          variant="outlined"
          filter
        ></v-chip>

        <v-chip
          text="Wheelchair access"
          variant="outlined"
          filter
        ></v-chip>

        <v-chip
          text="Dogs ok"
          variant="outlined"
          filter
        ></v-chip>

        <v-chip
          text="Cats ok"
          variant="outlined"
          filter
        ></v-chip>
      </v-chip-group>
    </v-card-text>

    <v-card-text>
      <h2 class="text-h6 mb-2">Choose neighborhoods</h2>

      <v-chip-group
        v-model="neighborhoods"
        column
        multiple
      >
        <v-chip
          text="Snowy Rock Place"
          variant="outlined"
          filter
        ></v-chip>

        <v-chip
          text="Honeylane Circle"
          variant="outlined"
          filter
        ></v-chip>

        <v-chip
          text="Donna Drive"
          variant="outlined"
          filter
        ></v-chip>

        <v-chip
          text="Elaine Street"
          variant="outlined"
          filter
        ></v-chip>

        <v-chip
          text="Court Street"
          variant="outlined"
          filter
        ></v-chip>

        <v-chip
          text="Kennedy Park"
          variant="outlined"
          filter
        ></v-chip>
      </v-chip-group>
    </v-card-text>
  </v-card>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const amenities = shallowRef([1, 4])
  const neighborhoods = shallowRef([1])
</script>

<script>
  export default {
    data: () => ({
      amenities: [1, 4],
      neighborhoods: [1],
    }),
  }
</script>

```

# Vuetify component v-chip-group - prop column

Example code

```vue
<template>
  <v-sheet
    class="mx-auto"
    elevation="10"
    max-width="300"
    rounded="xl"
  >
    <v-sheet
      class="pa-3 bg-primary text-right"
      rounded="t-xl"
    >
      <v-btn icon="mdi-content-save-cog-outline"></v-btn>

      <v-btn
        class="ms-2"
        icon="mdi-check-bold"
      ></v-btn>
    </v-sheet>

    <div class="pa-4">
      <v-chip-group
        selected-class="text-primary"
        column
      >
        <v-chip
          v-for="tag in tags"
          :key="tag"
        >
          {{ tag }}
        </v-chip>
      </v-chip-group>
    </div>
  </v-sheet>
</template>

<script setup>
  const tags = [
    'Work',
    'Home Improvement',
    'Vacation',
    'Food',
    'Drawers',
    'Shopping',
    'Art',
    'Tech',
    'Creative Writing',
  ]
</script>

<script>
  export default {
    data: () => ({
      tags: [
        'Work',
        'Home Improvement',
        'Vacation',
        'Food',
        'Drawers',
        'Shopping',
        'Art',
        'Tech',
        'Creative Writing',
      ],
    }),
  }
</script>

```

# Vuetify component v-chip-group - prop multiple

Example code

```vue
<template>
  <v-sheet class="py-4 px-1">
    <v-chip-group
      selected-class="text-primary"
      multiple
    >
      <v-chip
        v-for="tag in tags"
        :key="tag"
        :text="tag"
      ></v-chip>
    </v-chip-group>
  </v-sheet>
</template>

<script setup>
  const tags = [
    'Work',
    'Home Improvement',
    'Vacation',
    'Food',
    'Drawers',
    'Shopping',
    'Art',
    'Tech',
    'Creative Writing',
  ]
</script>

<script>
  export default {
    data: () => ({
      tags: [
        'Work',
        'Home Improvement',
        'Vacation',
        'Food',
        'Drawers',
        'Shopping',
        'Art',
        'Tech',
        'Creative Writing',
      ],
    }),
  }
</script>

```

# Vuetify component v-chip-group - prop mandatory

Example code

```vue
<template>
  <v-sheet class="py-4 px-1">
    <v-chip-group
      selected-class="text-primary"
      mandatory
    >
      <v-chip
        v-for="tag in tags"
        :key="tag"
        :text="tag"
      ></v-chip>
    </v-chip-group>
  </v-sheet>
</template>

<script setup>
  const tags = [
    'Work',
    'Home Improvement',
    'Vacation',
    'Food',
    'Drawers',
    'Shopping',
    'Art',
    'Tech',
    'Creative Writing',
  ]
</script>

<script>
  export default {
    data: () => ({
      tags: [
        'Work',
        'Home Improvement',
        'Vacation',
        'Food',
        'Drawers',
        'Shopping',
        'Art',
        'Tech',
        'Creative Writing',
      ],
    }),
  }
</script>

```

# Vuetify component v-chip-group - misc toothbrush card

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-card-title class="d-flex">
      <h2 class="text-h4">Toothbrush</h2>

      <v-spacer></v-spacer>

      <span class="text-h6">$4.99</span>
    </v-card-title>

    <v-card-text>
      Our company takes pride in making handmade brushes.
      Our toothbrushes are available in 4 different bristel types, from extra soft to hard.
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-text>
      <span class="subheading">Select type</span>

      <v-chip-group
        v-model="selection"
        variant="flat"
        mandatory
      >
        <v-chip text="Extra Soft" border></v-chip>
        <v-chip text="Soft" border></v-chip>
        <v-chip text="Medium" border></v-chip>
        <v-chip text="Hard" border></v-chip>
      </v-chip-group>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="secondary"
        text="Add to Cart"
        variant="flat"
        block
      ></v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const selection = shallowRef(2)
</script>

<script>
  export default {
    data: () => ({
      selection: 2,
    }),
  }
</script>

```

# Vuetify component v-chip-group - misc reddit categories

Example code

```vue
<template>
  <v-sheet
    class="mx-auto"
    max-width="400"
    rounded="xl"
    border
  >
    <div class="pa-4">
      <div class="text-h6">What are you into?</div>

      <div class="text-subtitle-1">Select topics to continue</div>

      <v-responsive class="overflow-y-auto" max-height="280">
        <v-chip-group class="mt-3" column>
          <v-chip
            v-for="topic in topics"
            :key="topic"
            :text="topic"
            :value="topic"
          ></v-chip>
        </v-chip-group>
      </v-responsive>
    </div>

    <v-divider></v-divider>

    <div class="pa-2">
      <v-btn
        color="orange-darken-1"
        rounded="t-0 b-xl"
        size="x-large"
        text="Continue"
        variant="flat"
        block
      ></v-btn>
    </div>
  </v-sheet>
</template>

<script setup>
  const topics = [
    '🎤 Advice',
    '🐕 Animals',
    '🤖 Anime',
    '🎨 Art & Design',
    '💄 Beauty',
    '🏢 Business',
    '📚 Books',
    '💡 Damn That\'s Interesting',
    '💃 Hobbies',
    '🎮 Gaming',
    '🎥 Movies',
    '🎵 Music',
    '📺 TV',
    '🌮 Food',
    '😂 Funny',
    '💖 Health & Lifestyle',
    '🎓 School',
    '📰 News',
    '🌲 Nature',
    '🎨 Photography',
    '🎏 Sports',
  ]
</script>

<script>
  export default {
    data: () => ({
      topics: [
        '🎤 Advice',
        '🐕 Animals',
        '🤖 Anime',
        '🎨 Art & Design',
        '💄 Beauty',
        '🏢 Business',
        '📚 Books',
        '💡 Damn That\'s Interesting',
        '💃 Hobbies',
        '🎮 Gaming',
        '🎥 Movies',
        '🎵 Music',
        '📺 TV',
        '🌮 Food',
        '😂 Funny',
        '💖 Health & Lifestyle',
        '🎓 School',
        '📰 News',
        '🌲 Nature',
        '🎨 Photography',
        '🎏 Sports',
      ],
    }),
  }
</script>

```

# Vuetify component v-chip-group - misc product card

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-card-title class="d-flex">
      <h2 class="text-h4">Shirt Blouse</h2>

      <v-spacer></v-spacer>

      <span class="text-h6">$44.50</span>
    </v-card-title>

    <v-card-text>
      Our blouses are available in 8 colors. You can custom order a built-in arch support for any of the models.
    </v-card-text>

    <v-divider class="mx-4"></v-divider>

    <v-card-text>
      <span class="subheading">Select size</span>

      <v-chip-group
        v-model="selection"
        selected-class="text-deep-purple-accent-4"
        mandatory
      >
        <v-chip
          v-for="size in sizes"
          :key="size"
          :text="size"
          :value="size"
          variant="outlined"
        ></v-chip>
      </v-chip-group>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="deep-purple-accent-4"
        text="Add to Cart"
        variant="flat"
        block
      ></v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const sizes = [
    '04',
    '06',
    '08',
    '10',
    '12',
    '14',
  ]

  const selection = ref('08')
</script>

<script>
  export default {
    data: () => ({
      selection: '08',
      sizes: [
        '04', '06', '08', '10', '12', '14',
      ],
    }),
  }
</script>

```
