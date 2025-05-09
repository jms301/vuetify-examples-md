# Vuetify concept accessibility - menu

Example code

```vue
<template>
  <div class="text-center">
    <v-menu>
      <template v-slot:activator="{ props: activatorProps }">
        <v-btn text="Click me" v-bind="activatorProps"></v-btn>
      </template>

      <v-list>
        <v-list-item @click="onClick">
          <v-list-item-title>Option 1</v-list-item-title>
        </v-list-item>

        <v-list-item disabled>
          <v-list-item-title>Option 2</v-list-item-title>
        </v-list-item>

        <v-list-item @click="onClick">
          <v-list-item-title>Option 3</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

<script setup>
  function onClick () {
        // Perform an action
  }
</script>

<script>
  export default {
    methods: {
      onClick () {
        // Perform an action
      },
    },
  }
</script>

```

# Vuetify concept accessibility - select list item

Example code

```vue
<template>
  <v-select
    :items="['Foo', 'Bar', 'Fizz', 'Buzz']"
    label="Fizzbuzz"
  >
    <template v-slot:item="{ item, props }">
      <v-list-item v-bind="props">
        <template v-slot:title>
          {{ item.raw }}
        </template>
      </v-list-item>
    </template>
  </v-select>
</template>

```

# Vuetify concept accessibility - list item group

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="500"
  >
    <v-list v-model="model">
      <v-list-item
        v-for="(item, i) in items"
        :key="i"
        :disabled="item.disabled"
        :title="item.text"
        :value="item"
      ></v-list-item>
    </v-list>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const items = [
    {
      text: 'Item 1',
      disabled: false,
    },
    {
      text: 'Item 2',
      disabled: true,
    },
    {
      text: 'Item 3',
      disabled: false,
    },
  ]

  const model = ref(0)
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          text: 'Item 1',
          disabled: false,
        },
        {
          text: 'Item 2',
          disabled: true,
        },
        {
          text: 'Item 3',
          disabled: false,
        },
      ],
      model: 0,
    }),
  }
</script>

```
