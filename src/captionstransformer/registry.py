from captionstransformer import transcript, ttml, sbv, srt, sami

REGISTRY = {'transcript':{'id': 'transcript',
                          'reader': transcript.Reader,
                          'writer': transcript.Writer,
                          'mimetype': 'text/xml',
                          'extension': '.xml'},
            'TTML':{'id': 'TTML',
                    'reader': ttml.Reader,
                    'writer': ttml.Writer,
                    'mimetype': 'application/ttml+xml',
                    'extension': '.xml'},
            'SBV': {'id': 'SBV',
                    'reader': sbv.Reader,
                    'writer': sbv.Writer,
                    'mimetype': 'text/plain',
                    'extension': '.sbv'},
            'SRT': {'id': 'SRT',
                    'reader': srt.Reader,
                    'writer': srt.Writer,
                    'mimetype': 'text/plain',
                    'extension': '.srt'}}
            'SAMI': {'id': 'SAMI',
                    'reader': sami.Reader,
                    'writer': sami.Writer,
                    'mimetype': 'text/plain',
                    'extension': '.smi'}}
