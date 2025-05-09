# Vuetify component v-virtual-scroll - usage

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
      <v-virtual-scroll v-bind="props" :items="items">
        <template v-slot:default="{ item }">
          Item {{ item }}
        </template>
      </v-virtual-scroll>
    </div>

    <!-- <template v-slot:configuration>
    </template> -->
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-virtual-scroll'
  const model = ref('default')
  const items = Array.from({ length: 1000 }, (k, v) => v + 1)
  const options = []
  const props = computed(() => {
    return {
      height: 300,
      items: Array.from({ length: 1000 }, (k, v) => v + 1).slice(0, 30),
    }
  })

  const slots = computed(() => {
    return `
  <template v-slot:default="{ item }">
    Item {{ item }}
  </template>
`
  })

  const code = computed(() => {
    return `<${name}${propsToString(props.value)}>${slots.value}</${name}>`
  })
</script>

```

# Vuetify component v-virtual-scroll - misc user directory

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-card-item class="bg-orange-darken-4">
      <v-card-title>
        User Directory
      </v-card-title>

      <template v-slot:append>
        <v-btn
          color="white"
          icon="mdi-plus"
          size="small"
        ></v-btn>
      </template>
    </v-card-item>

    <v-card-text class="pt-4">
      Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quasi nobis a at voluptates culpa optio amet! Inventore deserunt voluptatem maxime a veniam placeat, eos impedit nulla quos? Officiis, aperiam ducimus.
    </v-card-text>

    <v-divider></v-divider>

    <v-virtual-scroll
      :items="items"
      height="300"
      item-height="50"
    >
      <template v-slot:default="{ item }">
        <v-list-item>
          <template v-slot:prepend>
            <v-avatar
              :color="item.color"
              class="text-white"
              size="40"
            >
              {{ item.initials }}
            </v-avatar>
          </template>

          <v-list-item-title>{{ item.fullName }}</v-list-item-title>

          <template v-slot:append>
            <v-btn
              size="small"
              variant="tonal"
            >
              View User

              <v-icon
                color="orange-darken-4"
                end
              >
                mdi-open-in-new
              </v-icon>
            </v-btn>
          </template>
        </v-list-item>
      </template>
    </v-virtual-scroll>
  </v-card>
</template>

<script setup>
  import { computed } from 'vue'

  const colors = ['#2196F3', '#90CAF9', '#64B5F6', '#42A5F5', '#1E88E5', '#1976D2', '#1565C0', '#0D47A1', '#82B1FF', '#448AFF', '#2979FF', '#2962FF']
  const names = ['Oliver', 'Jake', 'Noah', 'James', 'Jack', 'Connor', 'Liam', 'John', 'Harry', 'Callum', 'Mason', 'Robert', 'Jacob', 'Jacob', 'Jacob', 'Michael', 'Charlie', 'Kyle', 'William', 'William', 'Thomas', 'Joe', 'Ethan', 'David', 'George', 'Reece', 'Michael', 'Richard', 'Oscar', 'Rhys', 'Alexander', 'Joseph', 'James', 'Charlie', 'James', 'Charles', 'William', 'Damian', 'Daniel', 'Thomas', 'Amelia', 'Margaret', 'Emma', 'Mary', 'Olivia', 'Samantha', 'Olivia', 'Patricia', 'Isla', 'Bethany']
  const surnames = ['Smith', 'Anderson', 'Clark', 'Wright', 'Mitchell', 'Johnson', 'Thomas', 'Rodriguez', 'Lopez', 'Perez', 'Williams', 'Jackson', 'Lewis', 'Hill', 'Roberts', 'Jones', 'White', 'Lee', 'Scott', 'Turner', 'Brown', 'Harris', 'Walker', 'Green', 'Phillips', 'Davis', 'Martin', 'Hall', 'Adams', 'Campbell', 'Miller', 'Thompson', 'Allen', 'Baker', 'Parker', 'Wilson', 'Garcia', 'Young', 'Gonzalez', 'Evans', 'Moore', 'Martinez', 'Hernandez', 'Nelson', 'Edwards', 'Taylor', 'Robinson', 'King', 'Carter', 'Collins']

  const items = computed(() => {
    const namesLength = names.length
    const surnamesLength = surnames.length
    const colorsLength = colors.length

    return Array.from({ length: 10000 }, () => {
      const name = names[genRandomIndex(namesLength)]
      const surname = surnames[genRandomIndex(surnamesLength)]

      return {
        color: colors[genRandomIndex(colorsLength)],
        fullName: `${name} ${surname}`,
        initials: `${name[0]} ${surname[0]}`,
      }
    })
  })

  function genRandomIndex (length) {
    return Math.ceil(Math.random() * (length - 1))
  }
</script>

<script>
  export default {
    data: () => ({
      colors: ['#2196F3', '#90CAF9', '#64B5F6', '#42A5F5', '#1E88E5', '#1976D2', '#1565C0', '#0D47A1', '#82B1FF', '#448AFF', '#2979FF', '#2962FF'],
      names: ['Oliver', 'Jake', 'Noah', 'James', 'Jack', 'Connor', 'Liam', 'John', 'Harry', 'Callum', 'Mason', 'Robert', 'Jacob', 'Jacob', 'Jacob', 'Michael', 'Charlie', 'Kyle', 'William', 'William', 'Thomas', 'Joe', 'Ethan', 'David', 'George', 'Reece', 'Michael', 'Richard', 'Oscar', 'Rhys', 'Alexander', 'Joseph', 'James', 'Charlie', 'James', 'Charles', 'William', 'Damian', 'Daniel', 'Thomas', 'Amelia', 'Margaret', 'Emma', 'Mary', 'Olivia', 'Samantha', 'Olivia', 'Patricia', 'Isla', 'Bethany'],
      surnames: ['Smith', 'Anderson', 'Clark', 'Wright', 'Mitchell', 'Johnson', 'Thomas', 'Rodriguez', 'Lopez', 'Perez', 'Williams', 'Jackson', 'Lewis', 'Hill', 'Roberts', 'Jones', 'White', 'Lee', 'Scott', 'Turner', 'Brown', 'Harris', 'Walker', 'Green', 'Phillips', 'Davis', 'Martin', 'Hall', 'Adams', 'Campbell', 'Miller', 'Thompson', 'Allen', 'Baker', 'Parker', 'Wilson', 'Garcia', 'Young', 'Gonzalez', 'Evans', 'Moore', 'Martinez', 'Hernandez', 'Nelson', 'Edwards', 'Taylor', 'Robinson', 'King', 'Carter', 'Collins'],
    }),

    computed: {
      items () {
        const namesLength = this.names.length
        const surnamesLength = this.surnames.length
        const colorsLength = this.colors.length

        return Array.from({ length: 10000 }, () => {
          const name = this.names[this.genRandomIndex(namesLength)]
          const surname = this.surnames[this.genRandomIndex(surnamesLength)]

          return {
            color: this.colors[this.genRandomIndex(colorsLength)],
            fullName: `${name} ${surname}`,
            initials: `${name[0]} ${surname[0]}`,
          }
        })
      },
    },

    methods: {
      genRandomIndex (length) {
        return Math.ceil(Math.random() * (length - 1))
      },
    },
  }
</script>

```

# Vuetify component v-virtual-scroll - prop dynamic item height

Example code

```vue
<template>
  <v-virtual-scroll
    :items="items"
    height="400"
  >
    <template v-slot:default="{ item, index }">
      <div
        :class="[
          index % 2 === 0 ? 'py-2' : index % 5 == 0 ? 'py-8' : 'py-4',
          index % 2 === 0 ? 'bg-grey-lighten-2' : index % 5 === 0 ? 'bg-grey-darken-2' : '',
          'px-2'
        ]"
      >
        Dynamic item {{ item }}
      </div>
    </template>
  </v-virtual-scroll>
</template>

<script setup>
  const items = Array.from({ length: 1000 }, (k, v) => v + 1)
</script>

<script>
  export default {
    computed: {
      items () {
        return Array.from({ length: 1000 }, (k, v) => v + 1)
      },
    },
  }
</script>

```

# Vuetify component v-virtual-scroll - prop height

Example code

```vue
<template>
  <v-virtual-scroll :items="items" height="200">
    <template v-slot:default="{ item }">
      Virtual Item {{ item }}
    </template>
  </v-virtual-scroll>
</template>

<script setup>
  const items = Array.from({ length: 1000 }, (k, v) => v + 1)
</script>

<script>
  export default {
    data: () => ({
      items: Array.from({ length: 1000 }, (k, v) => v + 1),
    }),
  }
</script>

```

# Vuetify component v-virtual-scroll - prop item height

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="500"
  >
    <v-card-title>
      Company Employee List
    </v-card-title>

    <v-divider></v-divider>

    <v-virtual-scroll
      :items="items"
      height="320"
      item-height="48"
    >
      <template v-slot:default="{ item }">
        <v-list-item
          :subtitle="`Badge #${item}`"
          :title="`Employee Name`"
        >
          <template v-slot:prepend>
            <v-icon class="bg-primary">mdi-account</v-icon>
          </template>

          <template v-slot:append>
            <v-btn
              icon="mdi-pencil"
              size="x-small"
              variant="tonal"
            ></v-btn>
          </template>
        </v-list-item>
      </template>
    </v-virtual-scroll>
  </v-card>
</template>

<script setup>
  const items = Array.from({ length: 1000 }, (k, v) => v + 1)
</script>

<script>
  export default {
    data: () => ({
      items: Array.from({ length: 1000 }, (k, v) => v + 1),
    }),
  }
</script>

```

# Vuetify component v-virtual-scroll - prop height parent

Example code

```vue
<template>
  <div style="display: flex; height: 200px;">
    <v-virtual-scroll :items="items">
      <template v-slot:default="{ item }">
        Virtual Item {{ item }}
      </template>
    </v-virtual-scroll>
  </div>
</template>

<script setup>
  const items = Array.from({ length: 1000 }, (k, v) => v + 1)
</script>

<script>
  export default {
    data: () => ({
      items: Array.from({ length: 1000 }, (k, v) => v + 1),
    }),
  }
</script>

```
