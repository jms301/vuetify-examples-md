# Vuetify component v-alert - usage

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
      <v-alert
        v-if="alert"
        v-model="alert"
        v-bind="props"
      >
        <template v-slot:text>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!
        </template>
      </v-alert>

      <div class="text-center">
        <v-btn v-if="!alert" @click="alert = true">
          Show Alert
        </v-btn>
      </div>
    </div>

    <template v-slot:configuration>
      <v-select
        v-model="type"
        :items="[
          'success',
          'info',
          'warning',
          'error',
        ]"
        label="Type"
        clearable
      ></v-select>

      <v-checkbox v-model="title" label="Show title"></v-checkbox>

      <v-checkbox v-model="closable" label="Closable"></v-checkbox>

      <v-checkbox v-model="icon" label="Custom icon"></v-checkbox>
    </template>
  </ExamplesUsageExample>
</template>

<script setup>
  const name = 'v-alert'
  const model = ref('default')
  const alert = ref(true)
  const closable = ref(false)
  const icon = ref(false)
  const title = ref(false)
  const type = ref()
  const options = ['outlined', 'tonal']
  const props = computed(() => {
    return {
      closable: closable.value || undefined,
      icon: icon.value ? '$vuetify' : undefined,
      title: title.value ? 'Alert title' : undefined,
      text: '...',
      type: type.value || undefined,
      variant: ['outlined', 'tonal'].includes(model.value) ? model.value : undefined,
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

# Vuetify component v-alert - prop variant

Example code

```vue
<template>
  <v-alert
    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!"
    title="Alert title"
    type="info"
    variant="tonal"
  ></v-alert>
</template>

```

# Vuetify component v-alert - prop closable

Example code

```vue
<template>
  <div>
    <v-alert
      v-model="alert"
      border="start"
      close-label="Close Alert"
      color="deep-purple-accent-4"
      title="Closable Alert"
      variant="tonal"
      closable
    >
      Aenean imperdiet. Quisque id odio. Cras dapibus. Pellentesque ut neque. Cras dapibus.

      Vivamus consectetuer hendrerit lacus. Sed mollis, eros et ultrices tempus, mauris ipsum aliquam libero, non adipiscing dolor urna a orci. Sed mollis, eros et ultrices tempus, mauris ipsum aliquam libero, non adipiscing dolor urna a orci. Curabitur blandit mollis lacus. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo.
    </v-alert>

    <div
      v-if="!alert"
      class="text-center"
    >
      <v-btn @click="alert = true">
        Reset
      </v-btn>
    </div>
  </div>
</template>

<script setup>
  import { ref } from 'vue'

  const alert = ref(true)
</script>

<script>
  export default {
    data: () => ({
      alert: true,
    }),
  }
</script>

```

# Vuetify component v-alert - prop rounded

Example code

```vue
<template>
  <div>
    <v-alert
      rounded="0"
      title="Info"
      type="info"
    >
      I'm an alert with no rounded borders. Lorem ipsum dolor sit, amet consectetur adipisicing elit. Aspernatur recusandae, est itaque laboriosam amet officia? Officia repellat provident sed est adipisci voluptatibus, voluptas reprehenderit dicta voluptatum, optio enim, placeat nostrum.
    </v-alert>

    <br>

    <v-alert
      rounded="xl"
      title="Success"
      type="success"
      variant="outlined"
    >
      I'm an alert with extra large rounded borders. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Enim cumque vel sapiente suscipit officia ullam quam possimus provident id neque, cupiditate fuga animi expedita, beatae ipsam in veniam inventore totam.
    </v-alert>

    <br>

    <v-alert
      rounded="pill"
      title="Warning"
      type="warning"
      prominent
    >
      I'm an alert with pill rounded borders. Lorem ipsum dolor sit amet consectetur adipisicing elit. Laudantium ex excepturi ea odio cum libero animi vitae repellat fuga velit explicabo quae, ducimus.
    </v-alert>

    <br>

    <v-alert
      rounded="t-xl b-lg"
      title="Error"
      type="error"
      prominent
    >
      I'm an alert with top and bottom borders. Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rerum esse quis eius delectus odio repellat voluptates ullam doloribus eaque dignissimos
    </v-alert>
  </div>
</template>

```

# Vuetify component v-alert - prop icon

Example code

```vue
<template>
  <div>
    <v-alert
      color="#2A3B4D"
      density="compact"
      icon="mdi-firework"
      theme="dark"
    >
      Suspendisse enim turpis, dictum sed, iaculis a, condimentum nec, nisi. Vivamus quis mi. Quisque ut nisi. Maecenas malesuada.
    </v-alert>

    <br>

    <v-alert
      color="#C51162"
      icon="mdi-material-design"
      theme="dark"
      border
    >
      Phasellus blandit leo ut odio. Morbi mattis ullamcorper velit. Donec orci lectus, aliquam ut, faucibus non, euismod id, nulla. In ut quam vitae odio lacinia tincidunt.
    </v-alert>

    <br>

    <v-alert
      color="primary"
      icon="$vuetify"
      theme="dark"
      prominent
    >
      Praesent congue erat at massa. Nullam vel sem. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Proin viverra, ligula sit amet ultrices semper, ligula arcu tristique sapien, a accumsan nisi mauris ac eros. Curabitur at lacus ac velit ornare lobortis.
    </v-alert>
  </div>
</template>

```

# Vuetify component v-alert - prop density

Example code

```vue
<template>
  <v-alert
    density="compact"
    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!"
    title="Alert title"
    type="warning"
  ></v-alert>
</template>

```

# Vuetify component v-alert - prop outlined

Example code

```vue
<template>
  <div>
    <v-alert
      color="purple"
      variant="outlined"
    >
      <template v-slot:title>
        Outlined Alert
      </template>

      Maecenas ullamcorper, dui et placerat feugiat, eros pede varius nisi, condimentum viverra felis nunc et lorem. Duis vel nibh at velit scelerisque suscipit. Praesent blandit laoreet nibh. Aenean posuere, tortor sed cursus feugiat, nunc augue blandit nunc, eu sollicitudin urna dolor sagittis lacus. Etiam sollicitudin, ipsum eu pulvinar rutrum, tellus ipsum laoreet sapien, quis venenatis ante odio sit amet eros.
    </v-alert>

    <br>

    <v-alert
      type="success"
      variant="outlined"
    >
      Praesent venenatis metus at tortor pulvinar varius. Aenean commodo ligula eget dolor. Praesent ac massa at ligula laoreet iaculis. Vestibulum ullamcorper mauris at ligula.
    </v-alert>

    <br>

    <v-alert
      border="top"
      type="warning"
      variant="outlined"
      prominent
    >
      Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis, ipsum. Suspendisse non nisl sit amet velit hendrerit rutrum. Nullam vel sem. Pellentesque dapibus hendrerit tortor.
    </v-alert>
  </div>
</template>

```

# Vuetify component v-alert - prop type

Example code

```vue
<template>
  <v-alert
    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!"
    title="Alert title"
    type="success"
  ></v-alert>
</template>

```

# Vuetify component v-alert - prop content

Example code

```vue
<template>
  <v-alert
    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!"
    title="Alert title"
  ></v-alert>
</template>

```

# Vuetify component v-alert - prop border

Example code

```vue
<template>
  <div>
    <v-alert
      border="top"
      color="primary"
    >
      I'm an alert with a top border and primary color
    </v-alert>

    <br>

    <v-alert
      border="end"
      color="secondary"
    >
      I'm an alert with an end border and secondary color
    </v-alert>

    <br>

    <v-alert
      border="bottom"
      color="success"
    >
      I'm an alert with a bottom border and success color
    </v-alert>

    <br>

    <v-alert
      border="start"
      color="error"
    >
      I'm an alert with a start border and error color
    </v-alert>
  </div>
</template>

```

# Vuetify component v-alert - prop prominent

Example code

```vue
<template>
  <div>
    <v-alert
      type="error"
      prominent
    >
      <template v-slot:text>
        Nunc nonummy metus. Nunc interdum lacus sit amet orci Nullam dictum felis eu pede.
      </template>

      <template v-slot:append>
        <v-btn size="small" variant="text">Take action</v-btn>
      </template>
    </v-alert>

    <br>

    <v-alert
      color="blue-grey-darken-2"
      density="compact"
      icon="mdi-school"
      prominent
    >
      Sed augue ipsum, egestas nec, vestibulum et, malesuada adipiscing, dui. Aenean ut eros et nisl sagittis vestibulum. Sed aliquam ultrices mauris. Donec vitae orci sed dolor rutrum auctor.
    </v-alert>

    <br>

    <v-alert
      icon="mdi-shield-lock-outline"
      type="info"
      prominent
    >
      Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Sed in libero ut nibh placerat accumsan.. Curabitur blandit mollis lacus. Curabitur blandit mollis lacus.
    </v-alert>
  </div>
</template>

```

# Vuetify component v-alert - prop border color

Example code

```vue
<template>
  <div>
    <v-alert
      border="start"
      border-color="deep-purple accent-4"
      elevation="2"
    >
      Aliquam eu nunc. Fusce commodo aliquam arcu. In consectetuer turpis ut velit. Nulla facilisi..

      Morbi mollis tellus ac sapien. Fusce vel dui. Praesent ut ligula non mi varius sagittis. Vivamus consectetuer hendrerit lacus. Suspendisse enim turpis, dictum sed, iaculis a, condimentum nec, nisi.
    </v-alert>

    <br>

    <v-alert
      border="top"
      border-color="success"
      elevation="2"
    >
      Vestibulum ullamcorper mauris at ligula. Nam pretium turpis et arcu. Ut varius tincidunt libero. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet, leo. Morbi nec metus.
    </v-alert>

    <br>

    <v-alert
      border="bottom"
      border-color="warning"
      elevation="2"
    >
      Sed in libero ut nibh placerat accumsan. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi. Phasellus leo dolor, tempus non, auctor et, hendrerit quis, nisi. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc, quis gravida magna mi a libero. Donec elit libero, sodales nec, volutpat a, suscipit non, turpis.
    </v-alert>

    <br>

    <v-alert
      border="end"
      border-color="error"
      elevation="2"
    >
      Fusce commodo aliquam arcu. Pellentesque posuere. Phasellus tempus. Donec posuere vulputate arcu.
    </v-alert>
  </div>
</template>

```
