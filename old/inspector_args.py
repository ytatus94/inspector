from inputargs import InputArgs

class InspectorArgs(InputArgs):
    def __init__(self, default_args, parser_obj=None):
        super().__init__(default_args)

        # arguments for inspector
        self.parser.add_argument(
            '--port',
            default=default_args.get('port'),
            type=int,
            help='Port for the dashboard',
        )
        # self.parser.add_argument(
        #     '--dashboard',
        #     default=default_args.get('dashboard'),
        #     type=str,
        #     required=True,
        #     help='Dashboard type: model, apni, simulator, forecast',
        #     choices=['model', 'apni', 'simulator', 'forecast'],
        # )

    def get_args(self):
        self.args = self.parser.parse_args()
        print(self.args)
        return self.args
