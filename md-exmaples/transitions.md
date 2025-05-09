# Vuetify concept transitions - usage

Example code

```vue
<template>
  <v-row justify="center">
    <v-menu transition="slide-x-transition">
      <template v-slot:activator="{ props }">
        <v-btn
          class="ma-2"
          color="primary"
          v-bind="props"
        >
          Slide X Transition
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="n in 5"
          :key="n"
          link
        >
          <v-list-item-title v-text="'Item ' + n"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

    <div class="mx-6 hidden-sm-and-down"></div>

    <v-menu transition="scroll-y-transition">
      <template v-slot:activator="{ props }">
        <v-btn
          class="ma-2"
          color="secondary"
          v-bind="props"
        >
          Scroll Y Transition
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="n in 5"
          :key="n"
          link
        >
          <v-list-item-title v-text="'Item ' + n"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-row>
</template>

```

# Vuetify concept transitions - misc fab

Example code

```vue
<template>
  <div class="text-center">
    <v-menu transition="fab-transition">
      <template v-slot:activator="{ props }">
        <v-btn
          color="primary"
          v-bind="props"
        >
          Fab Transition
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="n in 5"
          :key="n"
        >
          <v-list-item-title v-text="'Item ' + n"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

```

# Vuetify concept transitions - misc scroll x

Example code

```vue
<template>
  <v-row
    justify="center"
  >
    <v-menu transition="scroll-x-transition">
      <template v-slot:activator="{ props }">
        <v-btn
          class="ma-2"
          color="primary"
          v-bind="props"
        >
          Scroll X Transition
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="n in 5"
          :key="n"
          link
        >
          <v-list-item-title v-text="'Item ' + n"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

    <div class="mx-4 hidden-sm-and-down"></div>

    <v-menu transition="scroll-x-reverse-transition">
      <template v-slot:activator="{ props }">
        <v-btn
          class="ma-2"
          color="secondary"
          v-bind="props"
        >
          Scroll X Reverse Transition
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="n in 5"
          :key="n"
          link
        >
          <v-list-item-title v-text="'Item ' + n"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-row>
</template>

```

# Vuetify concept transitions - misc scroll y

Example code

```vue
<template>
  <v-row
    justify="center"
  >
    <v-menu transition="scroll-y-transition">
      <template v-slot:activator="{ props }">
        <v-btn
          class="ma-2"
          color="primary"
          v-bind="props"
        >
          Scroll Y Transition
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="n in 5"
          :key="n"
          link
        >
          <v-list-item-title v-text="'Item ' + n"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

    <div class="mx-4 hidden-sm-and-down"></div>

    <v-menu transition="scroll-y-reverse-transition">
      <template v-slot:activator="{ props }">
        <v-btn
          class="ma-2"
          color="secondary"
          v-bind="props"
        >
          Scroll Y Reverse Transition
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="n in 5"
          :key="n"
          link
        >
          <v-list-item-title v-text="'Item ' + n"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-row>
</template>

```

# Vuetify concept transitions - misc slide x

Example code

```vue
<template>
  <v-row
    justify="center"
  >
    <v-menu transition="slide-x-transition">
      <template v-slot:activator="{ props }">
        <v-btn
          class="ma-2"
          color="primary"
          v-bind="props"
        >
          Slide X Transition
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="n in 5"
          :key="n"
          link
        >
          <v-list-item-title v-text="'Item ' + n"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

    <div class="mx-4 hidden-sm-and-down"></div>

    <v-menu transition="slide-x-reverse-transition">
      <template v-slot:activator="{ props }">
        <v-btn
          class="ma-2"
          color="secondary"
          v-bind="props"
        >
          Slide X Reverse Transition
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="n in 5"
          :key="n"
          link
        >
          <v-list-item-title v-text="'Item ' + n"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-row>
</template>

```

# Vuetify concept transitions - misc fade

Example code

```vue
<template>
  <div class="text-center">
    <v-menu transition="fade-transition">
      <template v-slot:activator="{ props }">
        <v-btn
          color="primary"
          v-bind="props"
        >
          Fade Transition
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="n in 5"
          :key="n"
        >
          <v-list-item-title v-text="'Item ' + n"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

```

# Vuetify concept transitions - misc scale

Example code

```vue
<template>
  <div class="text-center">
    <v-menu transition="scale-transition">
      <template v-slot:activator="{ props }">
        <v-btn
          color="primary"
          v-bind="props"
        >
          Scale Transition
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="n in 5"
          :key="n"
        >
          <v-list-item-title v-text="'Item ' + n"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

```

# Vuetify concept transitions - misc slide y

Example code

```vue
<template>
  <v-row
    justify="center"
  >
    <v-menu transition="slide-y-transition">
      <template v-slot:activator="{ props }">
        <v-btn
          class="ma-2"
          color="primary"
          v-bind="props"
        >
          Slide Y Transition
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="n in 5"
          :key="n"
          link
        >
          <v-list-item-title v-text="'Item ' + n"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

    <div class="mx-4 hidden-sm-and-down"></div>

    <v-menu transition="slide-y-reverse-transition">
      <template v-slot:activator="{ props }">
        <v-btn
          class="ma-2"
          color="secondary"
          v-bind="props"
        >
          Slide Y Reverse Transition
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="n in 5"
          :key="n"
          link
        >
          <v-list-item-title v-text="'Item ' + n"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </v-row>
</template>

```

# Vuetify concept transitions - prop custom origin

Example code

```vue
<template>
  <div class="text-center">
    <v-menu
      origin="center center"
      transition="scale-transition"
    >
      <template v-slot:activator="{ props }">
        <v-btn
          color="primary"
          v-bind="props"
        >
          Scale Transition
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="n in 5"
          :key="n"
          @click="() => {}"
        >
          <v-list-item-title v-text="'Item ' + n"></v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

```

# Vuetify concept transitions - misc todo

Example code

```vue
<template>
  <v-container style="max-width: 500px">
    <v-text-field
      v-model="newTask"
      label="What are you working on?"
      variant="solo"
      @keydown.enter="create"
    >
      <template v-slot:append-inner>
        <v-fade-transition>
          <v-btn
            v-show="newTask"
            icon="mdi-plus-circle"
            variant="text"
            @click="create"
          ></v-btn>
        </v-fade-transition>
      </template>
    </v-text-field>

    <h2 class="text-h4 text-success ps-4">
      Tasks:&nbsp;
      <v-fade-transition leave-absolute>
        <span :key="`tasks-${tasks.length}`">
          {{ tasks.length }}
        </span>
      </v-fade-transition>
    </h2>

    <v-divider class="mt-4"></v-divider>

    <v-row
      align="center"
      class="my-1"
    >
      <strong class="mx-4 text-info-darken-2">
        Remaining: {{ remainingTasks }}
      </strong>

      <v-divider vertical></v-divider>

      <strong class="mx-4 text-success-darken-2">
        Completed: {{ completedTasks }}
      </strong>

      <v-spacer></v-spacer>

      <v-progress-circular
        v-model="progress"
        class="me-2"
      ></v-progress-circular>
    </v-row>

    <v-divider class="mb-4"></v-divider>

    <v-card v-if="tasks.length > 0">
      <v-slide-y-transition
        class="py-0"
        tag="v-list"
        group
      >
        <template v-for="(task, i) in tasks" :key="`${i}-${task.text}`">
          <v-divider
            v-if="i !== 0"
            :key="`${i}-divider`"
          ></v-divider>

          <v-list-item @click="task.done = !task.done">
            <template v-slot:prepend>
              <v-checkbox-btn v-model="task.done" color="grey"></v-checkbox-btn>
            </template>

            <v-list-item-title>
              <span :class="task.done ? 'text-grey' : 'text-primary'">{{ task.text }}</span>
            </v-list-item-title>

            <template v-slot:append>
              <v-expand-x-transition>
                <v-icon v-if="task.done" color="success">
                  mdi-check
                </v-icon>
              </v-expand-x-transition>
            </template>
          </v-list-item>
        </template>
      </v-slide-y-transition>
    </v-card>
  </v-container>
</template>
<script setup>
  import { computed, ref } from 'vue'

  const tasks = ref([
    {
      done: false,
      text: 'Foobar',
    },
    {
      done: false,
      text: 'Fizzbuzz',
    },
  ])
  const newTask = ref(null)

  const completedTasks = computed(() => {
    return tasks.value.filter(task => task.done).length
  })
  const progress = computed(() => {
    return completedTasks.value / tasks.value.length * 100
  })
  const remainingTasks = computed(() => {
    return tasks.value.length - completedTasks.value
  })

  function create () {
    tasks.value.push({
      done: false,
      text: newTask.value,
    })
    newTask.value = null
  }
</script>

<script>
  export default {
    data: () => ({
      tasks: [
        {
          done: false,
          text: 'Foobar',
        },
        {
          done: false,
          text: 'Fizzbuzz',
        },
      ],
      newTask: null,
    }),

    computed: {
      completedTasks () {
        return this.tasks.filter(task => task.done).length
      },
      progress () {
        return this.completedTasks / this.tasks.length * 100
      },
      remainingTasks () {
        return this.tasks.length - this.completedTasks
      },
    },

    methods: {
      create () {
        this.tasks.push({
          done: false,
          text: this.newTask,
        })

        this.newTask = null
      },
    },
  }
</script>

```

# Vuetify concept transitions - misc expand x

Example code

```vue
<template>
  <v-row
    justify="center"

    style="min-height: 160px;"
  >
    <v-col class="shrink">
      <v-btn
        class="ma-2"
        color="primary"
        @click="expand = !expand"
      >
        Expand Transition
      </v-btn>

      <v-expand-transition>
        <v-card
          v-show="expand"
          class="mx-auto bg-secondary"
          height="100"
          width="100"
        ></v-card>
      </v-expand-transition>
    </v-col>

    <div class="mx-4 hidden-sm-and-down"></div>

    <v-col class="shrink">
      <v-btn
        class="ma-2"
        color="secondary"
        @click="expand2 = !expand2"
      >
        Expand X Transition
      </v-btn>

      <v-expand-x-transition>
        <v-card
          v-show="expand2"
          class="mx-auto bg-secondary"
          height="100"
          width="100"
        ></v-card>
      </v-expand-x-transition>
    </v-col>
  </v-row>
</template>

<script setup>
  import { ref } from 'vue'

  const expand = ref(false)
  const expand2 = ref(false)
</script>

<script>
  export default {
    data: () => ({
      expand: false,
      expand2: false,
    }),
  }
</script>

```
