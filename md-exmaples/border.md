# Vuetify concept border - sides

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <v-col cols="auto">
        <div class="text-center">
          <div class="border border-t-lg" style="height: 64px; width: 64px;"></div>
          <div class="text-caption">border-t-lg</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <div class="border border-e-lg" style="height: 64px; width: 64px;"></div>
          <div class="text-caption">border-e-lg</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <div class="border border-b-lg" style="height: 64px; width: 64px;"></div>
          <div class="text-caption">border-b-lg</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <div class="border border-s-lg" style="height: 64px; width: 64px;"></div>
          <div class="text-caption">border-s-lg</div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept border - colors

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <v-col cols="auto">
        <div class="text-center">
          <v-sheet border="primary thin" class="mx-auto" height="64" width="64" rounded></v-sheet>
          <div class="text-caption">"primary thin"</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <v-sheet border="success sm" height="64" width="64" rounded></v-sheet>
          <div class="text-caption">"success sm"</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <v-sheet border="info md" height="64" width="64" rounded></v-sheet>
          <div class="text-caption">"info md"</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <v-sheet border="warning lg" height="64" width="64" rounded></v-sheet>
          <div class="text-caption">"warning lg"</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <v-sheet border="error xl" height="64" width="64" rounded></v-sheet>
          <div class="text-caption">"error xl"</div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept border - all

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <v-col cols="auto">
        <div class="text-center">
          <div class="border-thin" style="height: 64px; width: 64px;"></div>
          <div class="text-caption">border-thin</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <div class="border-sm" style="height: 64px; width: 64px;"></div>
          <div class="text-caption">border-sm</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <div class="border-md" style="height: 64px; width: 64px;"></div>
          <div class="text-caption">border-md</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <div class="border-lg" style="height: 64px; width: 64px;"></div>
          <div class="text-caption">border-lg</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <div class="border-xl" style="height: 64px; width: 64px;"></div>
          <div class="text-caption">border-xl</div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

```

# Vuetify concept border - card

Example code

```vue
<template>
  <v-container>
    <v-card
      border="opacity-50 sm"
      class="mx-auto"
      max-width="360"
      rounded="xl"
      variant="text"
    >
      <template v-slot:title>
        <div class="text-caption font-weight-bold">Revenue</div>
      </template>

      <template v-slot:append>
        <v-chip
          border="success sm opacity-100"
          color="green"
          size="small"
          variant="text"
        >
          <v-icon icon="mdi-arrow-up" start></v-icon> 13%
        </v-chip>
      </template>

      <template v-slot:text>
        <div class="text-h4 font-weight-black">$ 9,232,215</div>

        <small class="text-caption text-medium-emphasis d-flex justify-space-between align-center">
          <div>
            <span class="text-green">
              <v-avatar icon="mdi-arrow-up" size="small" variant="tonal"></v-avatar>
              + $ 3,295
            </span>

            in the last week
          </div>

          <v-btn
            icon="mdi-arrow-right"
            size="x-small"
            variant="text"
            border
          ></v-btn>
        </small>
      </template>
    </v-card>
  </v-container>
</template>

```

# Vuetify concept border - styles

Example code

```vue
<template>
  <v-container>
    <v-row justify="space-around">
      <v-col cols="auto">
        <div class="text-center">
          <v-btn text="Button A" variant="text" border></v-btn>
          <div class="text-caption">border</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <v-btn border="dashed thin" text="Button A" variant="text"></v-btn>
          <div class="text-caption">border-dashed</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <v-btn border="dotted thin" text="Button A" variant="text"></v-btn>
          <div class="text-caption">border-dotted</div>
        </div>
      </v-col>

      <v-col cols="auto">
        <div class="text-center">
          <v-btn border="double lg" text="Button A" variant="text"></v-btn>
          <div class="text-caption">border-double</div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

```
