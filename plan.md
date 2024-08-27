```mermaid
graph TD;
    A[Start command] --> B[Check if batter is available];
    B --> C{Batter available?};
    C -->|Yes| D[Preheat waffle iron];
    C -->|No| E[Alert: Refill batter];
    D --> F[Pour batter onto waffle iron];
    F --> G[Close waffle iron];
    G --> H[Set timer];
    H --> I[Wait for timer to finish];
    I --> J[Open waffle iron];
    J --> K[Remove waffle];
    K --> L[Place waffle on serving plate];
    L --> M[Clean waffle iron];
    M --> N[Reset for next waffle];
    N --> B;
    E --> O[End];
