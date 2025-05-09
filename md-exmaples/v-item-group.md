# Vuetify component v-item-group - usage

Example code

```vue
<template>
  <v-item-group>
    <v-container>
      <v-row>
        <v-col
          v-for="n in 3"
          :key="n"
          cols="12"
          md="4"
        >
          <v-item v-slot="{ isSelected, toggle }">
            <v-card
              :color="isSelected ? 'primary' : ''"
              class="d-flex align-center"
              height="200"
              dark
              @click="toggle"
            >
              <v-scroll-y-transition>
                <div
                  v-if="isSelected"
                  class="text-h2 flex-grow-1 text-center"
                >
                  Selected
                </div>
              </v-scroll-y-transition>
            </v-card>
          </v-item>
        </v-col>
      </v-row>
    </v-container>
  </v-item-group>
</template>

<script></script>

```

# Vuetify component v-item-group - prop multiple

Example code

```vue
<template>
  <v-item-group multiple>
    <v-container>
      <v-row>
        <v-col
          v-for="n in 3"
          :key="n"
          cols="12"
          md="4"
        >
          <v-item v-slot="{ isSelected, toggle }">
            <v-card
              :color="isSelected ? 'primary' : ''"
              class="d-flex align-center"
              height="200"
              dark
              @click="toggle"
            >
              <v-scroll-y-transition>
                <div
                  class="text-h3 flex-grow-1 text-center"
                >
                  {{ isSelected ? 'Selected' : 'Click Me!' }}
                </div>
              </v-scroll-y-transition>
            </v-card>
          </v-item>
        </v-col>
      </v-row>
    </v-container>
  </v-item-group>
</template>

<script></script>

```

# Vuetify component v-item-group - prop mandatory

Example code

```vue
<template>
  <v-item-group mandatory>
    <v-container>
      <v-row>
        <v-col
          v-for="n in 3"
          :key="n"
          cols="12"
          md="4"
        >
          <v-item v-slot="{ isSelected, toggle }">
            <v-card
              :color="isSelected ? 'primary' : ''"
              class="d-flex align-center"
              height="200"
              dark
              @click="toggle"
            >
              <v-scroll-y-transition>
                <div
                  class="text-h3 flex-grow-1 text-center"
                >
                  {{ isSelected ? 'Selected' : 'Click Me!' }}
                </div>
              </v-scroll-y-transition>
            </v-card>
          </v-item>
        </v-col>
      </v-row>
    </v-container>
  </v-item-group>
</template>

<script></script>

```

# Vuetify component v-item-group - misc chips

Example code

```vue
<template>
  <v-card>
    <v-toolbar
      color="blue-grey"
      dark
      flat
    >
      <v-toolbar-title>Submit a post</v-toolbar-title>
    </v-toolbar>

    <v-card-text>
      <v-text-field
        label="Title"
        model-value="My new post"
        variant="filled"
      ></v-text-field>

      <v-textarea
        label="Text"
        model-value="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse"
        variant="filled"
      ></v-textarea>

      <v-divider class="my-2"></v-divider>

      <v-item-group selected-class="bg-purple" multiple>
        <div class="text-caption mb-2">Tags</div>
        <v-item
          v-for="n in 8"
          :key="n"
          v-slot="{ selectedClass, toggle }"
        >
          <v-chip
            :class="selectedClass"
            @click="toggle"
          >
            Tag {{ n }}
          </v-chip>
        </v-item>
      </v-item-group>
    </v-card-text>

    <v-divider></v-divider>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        color="success"
      >
        Post
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

```

# Vuetify component v-item-group - misc selection

Example code

```vue
<template>
  <v-card
    class="mx-auto"
    max-width="400"
  >
    <v-container class="pa-1">
      <v-item-group
        v-model="selection"
        multiple
      >
        <v-row>
          <v-col
            v-for="(item, i) in items"
            :key="i"
            cols="12"
            md="6"
          >
            <v-item v-slot="{ isSelected, toggle }">
              <v-img
                :src="`https://cdn.vuetifyjs.com/images/${item.src}`"
                class="text-right pa-2"
                height="150"
                cover
                @click="toggle"
              >
                <v-btn :icon="isSelected ? 'mdi-heart' : 'mdi-heart-outline'"></v-btn>
              </v-img>
            </v-item>
          </v-col>
        </v-row>
      </v-item-group>
    </v-container>
  </v-card>
</template>

<script setup>
  import { ref } from 'vue'

  const items = [
    {
      src: 'backgrounds/bg.jpg',
    },
    {
      src: 'backgrounds/md.jpg',
    },
    {
      src: 'backgrounds/bg-2.jpg',
    },
    {
      src: 'backgrounds/md2.jpg',
    },
  ]

  const selection = ref([])
</script>

<script>
  export default {
    data: () => ({
      items: [
        {
          src: 'backgrounds/bg.jpg',
        },
        {
          src: 'backgrounds/md.jpg',
        },
        {
          src: 'backgrounds/bg-2.jpg',
        },
        {
          src: 'backgrounds/md2.jpg',
        },
      ],
      selection: [],
    }),
  }
</script>

```

# Vuetify component v-item-group - prop selected class

Example code

```vue
<template>
  <v-item-group selected-class="bg-primary">
    <v-container>
      <v-row>
        <v-col
          v-for="n in 3"
          :key="n"
          cols="12"
          md="4"
        >
          <v-item v-slot="{ isSelected, selectedClass, toggle }">
            <v-card
              :class="['d-flex align-center', selectedClass]"
              height="200"
              dark
              @click="toggle"
            >
              <div
                class="text-h3 flex-grow-1 text-center"
              >
                {{ isSelected ? 'Selected' : 'Click Me!' }}
              </div>
            </v-card>
          </v-item>
        </v-col>
      </v-row>
    </v-container>
  </v-item-group>
</template>

<script></script>

```
