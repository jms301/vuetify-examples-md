# Vuetify concept opacity - misc hover

Example code

```vue
<template>
  <v-container>
    <v-hover v-slot="{ props: hoverProps, isHovering }">
      <v-card
        v-bind="hoverProps"
        :class="[
          'mx-auto',
          isHovering ? 'opacity-100' : 'opacity-50'
        ]"
        color="secondary"
        height="128"
        width="256"
        flat
      ></v-card>
    </v-hover>
  </v-container>
</template>

```

# Vuetify concept opacity - misc opacity

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <v-col cols="auto">
        <div class="text-center">
          <div class="bg-primary opacity-100" style="height: 64px; width: 64px;"></div>
          <div class="text-caption">opacity-100</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <div class="bg-primary opacity-80" style="height: 64px; width: 64px;"></div>
          <div class="text-caption">opacity-80</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <div class="bg-primary opacity-60" style="height: 64px; width: 64px;"></div>
          <div class="text-caption">opacity-60</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <div class="bg-primary opacity-40" style="height: 64px; width: 64px;"></div>
          <div class="text-caption">opacity-40</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <div class="bg-primary opacity-20" style="height: 64px; width: 64px;"></div>
          <div class="text-caption">opacity-20</div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

```
