# Vuetify component v-stepper-vertical - usage

Example code

```vue
<template>
  <ExamplesUsageExample
    v-model="model"
    :code="code"
    :name="name"
    :options="options"
  >
    <v-container>
      <v-stepper-vertical :items="items">
        <template v-slot:item.1>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!
        </template>

        <template v-slot:item.2>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!
        </template>

        <template v-slot:item.3>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!
        </template>
      </v-stepper-vertical>
    </v-container>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-stepper-vertical'
  const model = ref('default')
  const options = []

  const items = [
    'Step 1',
    'Step 2',
    'Step 3',
  ]
  const props = computed(() => {
    return {
      items: [
        'Step 1',
        'Step 2',
        'Step 3',
      ],
    }
  })

  const slots = computed(() => {
    return ''
  })

  const code = computed(() => {
    return `<v-stepper-vertical${propsToString(props.value)}>${slots.value}</v-stepper-vertical>`
  })
</script>

```

# Vuetify component v-stepper-vertical - slot actions

Example code

```vue
<template>
  <v-stepper-vertical>
    <template v-slot:default="{ step }">
      <v-stepper-vertical-item
        :complete="step > 1"
        subtitle="Personal details"
        title="Step one"
        value="1"
      >
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!

        <template v-slot:next="{ next }">
          <v-btn color="primary" @click="next"></v-btn>
        </template>

        <template v-slot:prev></template>
      </v-stepper-vertical-item>

      <v-stepper-vertical-item
        :complete="step > 2"
        subtitle="Contact Details"
        title="Step two"
        value="2"
      >
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!

        <template v-slot:next="{ next }">
          <v-btn color="primary" @click="next"></v-btn>
        </template>

        <template v-slot:prev="{ prev }">
          <v-btn variant="plain" @click="prev"></v-btn>
        </template>
      </v-stepper-vertical-item>

      <v-stepper-vertical-item
        subtitle="Confirmation"
        title="Step three"
        value="3"
        @click:next="onClickFinish"
      >
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!

        <template v-slot:next="{ next }">
          <v-btn color="primary" text="Finish" @click="next"></v-btn>
        </template>

        <template v-slot:prev="{ prev }">
          <v-btn v-if="!finished" variant="plain" @click="prev"></v-btn>

          <v-btn v-else text="Reset" variant="plain" @click="finished = false"></v-btn>
        </template>
      </v-stepper-vertical-item>
    </template>
  </v-stepper-vertical>
</template>

<script setup>
  import { shallowRef } from 'vue'

  const finished = shallowRef(false)

  function onClickFinish () {
    finished.value = true

    alert('Finished')
  }
</script>

<script>
  export default {
    data: () => ({
      finished: false,
    }),

    methods: {
      onClickFinish () {
        this.finished = true

        alert('Finished')
      },
    },
  }
</script>

```
