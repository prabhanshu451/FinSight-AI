FinSightAI - Final packaging notes

You asked for a final project zip with Prophet support and MP3s replaced. This final zip includes:

- Dockerfiles (Django & FastAPI) updated to install system packages commonly required to build Prophet and its dependencies (build-essential, gcc, g++, python3-dev, default-libgomp, libatlas-base-dev, etc).
- Notes in the Dockerfiles about installing cmdstan via cmdstanpy (optional). Installing cmdstan at image build time will significantly increase image size. Consider installing cmdstan at runtime or using a prepared image.

Important remaining steps you should do locally before running in production:
1. Replace the placeholder sound files in `static/sounds/` with real MP3s under 50 KB:
   - chime_success.mp3
   - ping_warning.mp3

2. Make a copy of `.env.example` to `.env` and set real secrets (SECRET_KEY, DB credentials, SMTP, DOMAIN).

3. If you want Prophet to run inside the containers:
   - Ensure the Docker build succeeds (Prophet wheel may still need additional tooling).
   - Optionally install cmdstan (recommended): inside the container, run:
       pip install cmdstanpy
       python -c "import cmdstanpy; cmdstanpy.install_cmdstan()"
     This downloads cmdstan (hundreds of MB) — consider doing this in CI or a separate step.

4. Build & run:
   docker compose build
   docker compose up --build

Endpoints:
- Landing: http://localhost:8000/
- Dashboard: http://localhost:8000/dashboard/
- FastAPI Forecast: POST http://localhost:8001/forecast/{user_id}
- Flower: http://localhost:5555/

If you'd like, I can:
- Add small real MP3 beep files to the zip (I can generate tiny WAVs but encoding to MP3 reliably in this environment is limited).
- Add a CI Docker image that pre-installs cmdstan and Prophet binaries to avoid long builds.

Let me know if you want me to add prebuilt tiny MP3s or to add CMDSTAN install to the Docker build (I can add it but note it will make image very large).


# Loading demo data

To load demo users/expenses/forecasts after running migrations:

```
./seed_demo.sh
```
