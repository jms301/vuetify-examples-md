# Vuetify component v-parallax - usage

Example code

```vue
<template>
  <v-parallax src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"></v-parallax>
</template>

```

# Vuetify component v-parallax - misc content

Example code

```vue
<template>
  <v-parallax
    src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
  >
    <div class="d-flex flex-column fill-height justify-center align-center text-white">
      <h1 class="text-h4 font-weight-thin mb-4">
        Vuetify
      </h1>
      <h4 class="subheading">
        Build your application today!
      </h4>
    </div>
  </v-parallax>
</template>

```

# Vuetify component v-parallax - misc custom height

Example code

```vue
<template>
  <v-parallax
    height="300"
    src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg"
  ></v-parallax>
</template>

```

# Vuetify component v-parallax - misc welcome

Example code

```vue
<template>
  <v-parallax src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg">
    <v-container class="fill-height">
      <v-row
        class="justify-center align-center flex-column-reverse flex-md-row"
      >
        <v-col cols="12" md="6">
          <h1 class="text-h1 mb-8">John Doe</h1>
          <h3 class="text-h3 mb-8 font-weight-thin">Web Developer</h3>
          <v-btn class="elevation-4 rounded-xl mb-4" color="primary">
            Contact Me
          </v-btn>
        </v-col>
        <v-col class="text-center" cols="12" md="6">
          <v-avatar :size="300" class="elevation-12 mx-auto mb-8">
            <v-img src="https://randomuser.me/api/portraits/men/78.jpg"></v-img>
          </v-avatar>
        </v-col>
      </v-row>
    </v-container>
  </v-parallax>
</template>

```
