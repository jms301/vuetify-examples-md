# Vuetify component v-ripple - usage

Example code

```vue
<template>
  <div
    class="text-center elevation-2 pa-12 text-h5"
    v-ripple
  >
    HTML element with v-ripple
  </div>
</template>

```

# Vuetify component v-ripple - misc custom color

Example code

```vue
<template>
  <v-list>
    <v-list-item
      v-for="color in ['primary', 'secondary', 'info', 'success', 'warning', 'error']"
      :key="color"
      v-ripple="{ class: `text-${color}` }"
    >
      <v-list-item-title>Item with "{{ color }}" class</v-list-item-title>
    </v-list-item>
  </v-list>
</template>

```

# Vuetify component v-ripple - option center

Example code

```vue
<template>
  <div
    class="text-center elevation-2 pa-12 text-h5"
    v-ripple.center
  >
    HTML element with centered ripple
  </div>
</template>

```

# Vuetify component v-ripple - stop

Example code

```vue
<template>
  <v-row>
    <v-col cols="12">
      <v-card v-ripple>
        <v-card-text>Card with ripple</v-card-text>
        <v-card-actions>
          <v-btn>Button with ripple</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
    <v-col cols="12">
      <v-card v-ripple>
        <v-card-text>
          Outer card with ripple
          <v-card-actions>
            <v-card v-ripple.stop>
              <v-card-text>
                Inner card with <code>ripple.stop</code>
              </v-card-text>
            </v-card>
          </v-card-actions>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

```

# Vuetify component v-ripple - misc ripple in components

Example code

```vue
<script>
// TODO
// @ts-disable
</script>

<template>
  <v-row
    class="py-12"
    justify="space-around"
  >
    <v-btn
      color="primary"
    >
      With ripple (default)
    </v-btn>
    <v-btn
      :ripple="false"
      color="primary"
    >
      Without ripple
    </v-btn>
    <v-btn
      :ripple="{ class: 'text-red' }"
      variant="text"
    >
      With red ripple
    </v-btn>
  </v-row>
</template>

```
