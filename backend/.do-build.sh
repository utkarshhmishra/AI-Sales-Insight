# Build configuration for Digital Ocean App Platform
# This ensures proper build tools are available

# Install rust/cargo for tiktoken and pydantic-core
export CARGO_NET_GIT_FETCH_WITH_CLI=true

# Use pip with no binary for problematic packages if needed
# pip install --no-binary :all: tiktoken greenlet pydantic-core
