# Vuetify concept overflow - overflow

Example code

```vue
<template>
  <v-row>
    <v-col cols="auto">
      <v-card class="overflow-auto" height="200" width="200">
        <v-card-text>
          <h3>Overflow Auto</h3>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis
          facilis dicta esse molestias vero hic laudantium provident nisi eos
          quasi iusto alias sequi, aut aliquid voluptatibus commodi! Minima, eum
          voluptates?
        </v-card-text>
      </v-card>
    </v-col>

    <v-col cols="auto">
      <v-card class="overflow-hidden" height="200" width="200">
        <v-card-text>
          <h3>Overflow Hidden</h3>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis
          facilis dicta esse molestias vero hic laudantium provident nisi eos
          quasi iusto alias sequi, aut aliquid voluptatibus commodi! Minima, eum
          voluptates?
        </v-card-text>
      </v-card>
    </v-col>

    <v-col cols="auto">
      <v-card class="overflow-visible" height="200" width="200">
        <v-card-text>
          <h3>Overflow visible</h3>
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis
          facilis dicta esse molestias vero hic laudantium provident nisi eos
          quasi iusto alias sequi, aut aliquid voluptatibus commodi! Minima, eum
          voluptates?
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

```

# Vuetify concept overflow - overflow x

Example code

```vue
<template>
  <div style="width: 300px">
    <h3 class="mb-3">Overflow Auto</h3>
    <p class="overflow-x-auto bg-purple-lighten-5">
      QrLmmW69vMQDtCOg48jidqvvWD2FzDt7I7bBoDc98SRP5OwvOScVYbRzFdfp540eF5v1pjogYkyI8NXqu4wY8chgsXIV0LU7XQKWJ98wLaBSHWiBhvkEU1T3sd6KEFo53CLjVjIz8UvZajb8sbsu62xTsF9cRtFdwEvusq6zJHvedymDCUkY6qXHsuL6fOmHo4KKMurZuJZrK3plRPUaI8XVciz8dVq5CEUXjMrTcB76H1w90CnkRER3nYjs3suTa3223xs8aL97m0peQfjlvKbF8HcmQG5mHEitCn1QZnbMZUK3zE9AIjwcVXP7R9V4fw2A93cZD7wj333X6aaiHZdkkTPtst0u05KSob5c0ZuKQi4D3V395NfFKKr8cR27jmpB7dqK2GiWXeOQUFcjmFVwlHWSlH8ZdUoVJpXf1xL6CRUxwZP4EhBbqQZaJm26ijWII6LRxJ5eVU9Y7KKvQsUeX5BawtgeMWRmjeCwQadTLTQG8gLpi2DvGpMtPWCdqHgEglVSB1ZlDrjEEsXYrNx1IOY0053K3pWNaR1ezyz8kahRfNs3byaHcIQu9tWTrcMpBWhZ45DzLjVV1N8Zt96uLnNWK5DvbKW8GgMuwY7fHkZFz85MN4d2gL0j85HmXGx9oPTFRkPWsmMOHUvm5IhB7QqGSAwT1uL7HgBrNX9a1BAWrp9zV1IWAd1q65sKOOCxTZrXJDpxBxYE4rJAGU6pcri9mUf4g49ZiIAwfu9njtZyYimmImCa6TFhk2jQcSmFDHacExxqC2BfYATHFrKSy94dbw6uWT52nM7MSM9JDu4cs9cbfnaf6amt4hTUotCTONg604b8JKPI1sfd4CG36fBNcnErhpllfRlXkY1xFwmwZT7IJV8okPGNQdTKpdPJOBGw3LHMKojPJl1nPiQB5C9bdePFMNLejSXY5DDvO70ehOCJpBtKZY2quoFJJjGfXe8T4DuGYGmM6JYd5DNinWZuUWXGvfIlJRHgf8BQNQvtmEzqGXIeQZitiq9F
    </p>
    <h3 class="mb-3">Overflow Hidden</h3>
    <p class="overflow-x-hidden bg-deep-purple-lighten-5">
      QrLmmW69vMQDtCOg48jidqvvWD2FzDt7I7bBoDc98SRP5OwvOScVYbRzFdfp540eF5v1pjogYkyI8NXqu4wY8chgsXIV0LU7XQKWJ98wLaBSHWiBhvkEU1T3sd6KEFo53CLjVjIz8UvZajb8sbsu62xTsF9cRtFdwEvusq6zJHvedymDCUkY6qXHsuL6fOmHo4KKMurZuJZrK3plRPUaI8XVciz8dVq5CEUXjMrTcB76H1w90CnkRER3nYjs3suTa3223xs8aL97m0peQfjlvKbF8HcmQG5mHEitCn1QZnbMZUK3zE9AIjwcVXP7R9V4fw2A93cZD7wj333X6aaiHZdkkTPtst0u05KSob5c0ZuKQi4D3V395NfFKKr8cR27jmpB7dqK2GiWXeOQUFcjmFVwlHWSlH8ZdUoVJpXf1xL6CRUxwZP4EhBbqQZaJm26ijWII6LRxJ5eVU9Y7KKvQsUeX5BawtgeMWRmjeCwQadTLTQG8gLpi2DvGpMtPWCdqHgEglVSB1ZlDrjEEsXYrNx1IOY0053K3pWNaR1ezyz8kahRfNs3byaHcIQu9tWTrcMpBWhZ45DzLjVV1N8Zt96uLnNWK5DvbKW8GgMuwY7fHkZFz85MN4d2gL0j85HmXGx9oPTFRkPWsmMOHUvm5IhB7QqGSAwT1uL7HgBrNX9a1BAWrp9zV1IWAd1q65sKOOCxTZrXJDpxBxYE4rJAGU6pcri9mUf4g49ZiIAwfu9njtZyYimmImCa6TFhk2jQcSmFDHacExxqC2BfYATHFrKSy94dbw6uWT52nM7MSM9JDu4cs9cbfnaf6amt4hTUotCTONg604b8JKPI1sfd4CG36fBNcnErhpllfRlXkY1xFwmwZT7IJV8okPGNQdTKpdPJOBGw3LHMKojPJl1nPiQB5C9bdePFMNLejSXY5DDvO70ehOCJpBtKZY2quoFJJjGfXe8T4DuGYGmM6JYd5DNinWZuUWXGvfIlJRHgf8BQNQvtmEzqGXIeQZitiq9F
    </p>
    <h3 class="mb-3">Overflow visible</h3>
    <p class="overflow-x-visible bg-indigo-lighten-5">
      QrLmmW69vMQDtCOg48jidqvvWD2FzDt7I7bBoDc98SRP5OwvOScVYbRzFdfp540eF5v1pjogYkyI8NXqu4wY8chgsXIV0LU7XQKWJ98wLaBSHWiBhvkEU1T3sd6KEFo53CLjVjIz8UvZajb8sbsu62xTsF9cRtFdwEvusq6zJHvedymDCUkY6qXHsuL6fOmHo4KKMurZuJZrK3plRPUaI8XVciz8dVq5CEUXjMrTcB76H1w90CnkRER3nYjs3suTa3223xs8aL97m0peQfjlvKbF8HcmQG5mHEitCn1QZnbMZUK3zE9AIjwcVXP7R9V4fw2A93cZD7wj333X6aaiHZdkkTPtst0u05KSob5c0ZuKQi4D3V395NfFKKr8cR27jmpB7dqK2GiWXeOQUFcjmFVwlHWSlH8ZdUoVJpXf1xL6CRUxwZP4EhBbqQZaJm26ijWII6LRxJ5eVU9Y7KKvQsUeX5BawtgeMWRmjeCwQadTLTQG8gLpi2DvGpMtPWCdqHgEglVSB1ZlDrjEEsXYrNx1IOY0053K3pWNaR1ezyz8kahRfNs3byaHcIQu9tWTrcMpBWhZ45DzLjVV1N8Zt96uLnNWK5DvbKW8GgMuwY7fHkZFz85MN4d2gL0j85HmXGx9oPTFRkPWsmMOHUvm5IhB7QqGSAwT1uL7HgBrNX9a1BAWrp9zV1IWAd1q65sKOOCxTZrXJDpxBxYE4rJAGU6pcri9mUf4g49ZiIAwfu9njtZyYimmImCa6TFhk2jQcSmFDHacExxqC2BfYATHFrKSy94dbw6uWT52nM7MSM9JDu4cs9cbfnaf6amt4hTUotCTONg604b8JKPI1sfd4CG36fBNcnErhpllfRlXkY1xFwmwZT7IJV8okPGNQdTKpdPJOBGw3LHMKojPJl1nPiQB5C9bdePFMNLejSXY5DDvO70ehOCJpBtKZY2quoFJJjGfXe8T4DuGYGmM6JYd5DNinWZuUWXGvfIlJRHgf8BQNQvtmEzqGXIeQZitiq9F
    </p>
  </div>
</template>

```
