from aiogram.dispatcher.fsm.state import StatesGroup, State


class BotStates(StatesGroup):
    main_menu = State()
    choosing_installation_type = State()
    choosing_docker_steps = State()
    user_problem = State()
    req_info = State()


class InstallIssues:
    def __init__(self):
        self.help_mess = 'Try to find answer on your problem here:'
        self.docker_invalid_type = self.help_mess + 'https://forum.subspace.network/t/docker-install-invalid-type-issue/714'
        self.submitting_tx = self.help_mess + 'https://forum.subspace.network/t/error-submitting-transaction-to-the-pool/758'
        self.error_while_dialing = self.help_mess + 'https://forum.subspace.network/t/error-while-dialing-dns-telemetry-polkadot-io-tcp-443-x-parity-wss-submit-custom-kind-other-error-timeout/45'
        self.bootnode_not_connected = self.help_mess + 'https://forum.subspace.network/t/synchronization-does-not-start/733'
        self.farmer_stucked = self.help_mess + 'https://forum.subspace.network/t/farmer-got-stuck/805'
        self.node_is_unhealthy = self.help_mess + 'https://forum.subspace.network/t/docker-error-with-apple-chip/876'
        self.consensus_error_import_failed = self.help_mess + 'https://forum.subspace.network/t/consensus-error-import-failed-checking-inherents-failed-incorrectrootblockslist/327'
        self.error_importing_block = self.help_mess + 'https://forum.subspace.network/t/error-importing-block-0x0000-err-unknownparent/52'
        self.error_starting_userland_proxy = self.help_mess + 'https://forum.subspace.network/t/docker-installing-farmer-results-in-error-of-using-port-node/950'
        self.exported_method_subspaceapi_chain_constants = self.help_mess + 'https://forum.subspace.network/t/exported-method-subspaceapi-chain-constants-is-not-found/1007'
        self.invalid_transaction_validity = self.help_mess + 'https://forum.subspace.network/t/invalid-transaction-validity-invalidtransaction-stale/1056'
        self.cannot_allocate_memory = self.help_mess + 'https://forum.subspace.network/t/failed-to-allocate-bytes-exception-when-running-docker-on-aarch64/606'

