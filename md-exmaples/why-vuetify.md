# Vuetify concept why-vuetify - card components

Example code

```vue
<template>
  <v-card>
    <v-card-text>
      Lorem ipsum dolor sit amet <strong>consectetur</strong> adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! <span class="text-primary">Eaque cupiditate minima</span>, at placeat totam, <i>magni doloremque veniam neque</i> porro libero rerum unde voluptatem!
    </v-card-text>

    <v-card-title>Title</v-card-title>
  </v-card>
</template>

```

# Vuetify concept why-vuetify - card props

Example code

```vue
<template>
  <v-card
    text="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! Eaque cupiditate minima, at placeat totam, magni doloremque veniam neque porro libero rerum unde voluptatem!"
    title="Title"
  ></v-card>
</template>

```

# Vuetify concept why-vuetify - card slots

Example code

```vue
<template>
  <v-card>
    <template v-slot:title>
      Title
    </template>

    <template v-slot:text>
      Lorem ipsum dolor sit amet <strong>consectetur</strong> adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus! <span class="text-primary">Eaque cupiditate minima</span>, at placeat totam, <i>magni doloremque veniam neque</i> porro libero rerum unde voluptatem!
    </template>
  </v-card>
</template>

```
