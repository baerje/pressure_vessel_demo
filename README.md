# Pressure Vessel Mixer

An interactive animation that shows how pressures interact. Three sources push colored particles into a vessel, the particles mix, and the mixture leaves through an outlet valve and sprays into the open air.

- **Source A (red)** and **Source B (blue)** come in from the right, each through a hand valve.
- **Source C (green)** comes down the left side and into the bottom of the vessel through a one-way valve.
- The **outlet** leaves the top of the vessel and runs to the right.

Gauges show each source's pressure and the vessel's pressure, and two bars show the color mix inside the vessel and in the last 100 particles out. Scenario buttons set up common situations, such as one source overpowering the others or the outlet closed.

## How it behaves

- Pressures are in bar, 0 to 10. The vessel reads 10 bar when it holds 400 particles.
- A source flows only while its pressure is above the vessel's. It never flows backward.
- Inflow = 14 particles/s × hand valve opening × (source pressure − vessel pressure).
- Outflow = 16 particles/s × outlet valve opening × vessel pressure.

## Files

| Path | What it is |
| --- | --- |
| `index.html` | The page to host. Includes the settings for adding it to an iPad or iPhone home screen. |
| `apple-touch-icon.png`, `icon-512.png`, `manifest.webmanifest` | Home-screen icon and app settings. |
| `src/pressure-vessel.html` | The source of the page, as published to the Claude artifact. Edit this file. |
| `tools/build.py` | Rebuilds `index.html` and the icons from `src/`. |

## Making changes

1. Edit `src/pressure-vessel.html`.
2. Run `python3 tools/build.py` (needs Python 3 with Pillow for the icons).
3. Commit both the source and the rebuilt files.

To try it locally, open `index.html` in a browser.

## Hosting with GitHub Pages

In the repository's **Settings → Pages**, set the source to **Deploy from a branch**, branch `main`, folder `/ (root)`. The page appears at `https://<user>.github.io/pressure_vessel_demo/`. On an iPad, open that address in Safari and use **Share → Add to Home Screen** to get a full-screen app.

## Viewing tips

- **Full screen** (next to Pause) fills the screen with the diagram and its controls.
- On a phone, turn it sideways: the scenarios move into a menu and the controls stay on the diagram.
