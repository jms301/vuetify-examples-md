# Vuetify concept elevation - usage

Example code

```vue
<template>
  <v-container>
    <v-row justify="center">
      <v-col
        v-for="(_, n) in 25"
        :key="n"
        cols="auto"
      >
        <v-card
          :class="['d-flex justify-center align-center bg-secondary', `elevation-${n}`]"
          height="100"
          width="100"
        >
          <div>{{ n }}</div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept elevation - prop dynamic

Example code

```vue
<template>
  <div class="text--primary">
    <!-- Using the elevation prop -->
    <v-hover v-slot="{ isHovering, props }">
      <v-card
        v-bind="props"
        :elevation="isHovering ? 24 : 6"
        class="mx-auto pa-6"
      >
        Prop based elevation
      </v-card>
    </v-hover>

    <div class="my-6"></div>

    <!-- Using a dynamic class -->
    <v-hover v-slot="{ isHovering, props }">
      <div
        v-bind="props"
        :class="`elevation-${isHovering ? 24 : 6}`"
        class="mx-auto pa-6"
      >
        Class based elevation
      </div>
    </v-hover>
  </div>
</template>

```
