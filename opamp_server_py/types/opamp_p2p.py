# This is an automatically generated file, please do not change
# gen by protobuf_to_pydantic[v0.3.1.1](https://github.com/so1n/protobuf_to_pydantic)
# Protobuf Version: 5.29.4 
# Pydantic Version: 2.10.6 
from .anyvalue_p2p import KeyValue
from enum import IntEnum
from google.protobuf.message import Message  # type: ignore
from protobuf_to_pydantic.customer_validator import check_one_of
from pydantic import BaseModel
from pydantic import Field
from pydantic import model_validator
import typing

class AgentToServerFlags(IntEnum):
    AgentToServerFlags_Unspecified = 0
    AgentToServerFlags_RequestInstanceUid = 1


class ServerToAgentFlags(IntEnum):
    ServerToAgentFlags_Unspecified = 0
    ServerToAgentFlags_ReportFullState = 1
    ServerToAgentFlags_ReportAvailableComponents = 2


class ServerCapabilities(IntEnum):
    ServerCapabilities_Unspecified = 0
    ServerCapabilities_AcceptsStatus = 1
    ServerCapabilities_OffersRemoteConfig = 2
    ServerCapabilities_AcceptsEffectiveConfig = 4
    ServerCapabilities_OffersPackages = 8
    ServerCapabilities_AcceptsPackagesStatus = 16
    ServerCapabilities_OffersConnectionSettings = 32
    ServerCapabilities_AcceptsConnectionSettingsRequest = 64


class PackageType(IntEnum):
    """
     The type of the package, either an addon or a top-level package.
 Status: [Beta]
    """
    PackageType_TopLevel = 0
    PackageType_Addon = 1


class ServerErrorResponseType(IntEnum):
    ServerErrorResponseType_Unknown = 0
    ServerErrorResponseType_BadRequest = 1
    ServerErrorResponseType_Unavailable = 2


class CommandType(IntEnum):
    """
     Status: [Beta]
    """
    CommandType_Restart = 0


class AgentCapabilities(IntEnum):
    AgentCapabilities_Unspecified = 0
    AgentCapabilities_ReportsStatus = 1
    AgentCapabilities_AcceptsRemoteConfig = 2
    AgentCapabilities_ReportsEffectiveConfig = 4
    AgentCapabilities_AcceptsPackages = 8
    AgentCapabilities_ReportsPackageStatuses = 16
    AgentCapabilities_ReportsOwnTraces = 32
    AgentCapabilities_ReportsOwnMetrics = 64
    AgentCapabilities_ReportsOwnLogs = 128
    AgentCapabilities_AcceptsOpAMPConnectionSettings = 256
    AgentCapabilities_AcceptsOtherConnectionSettings = 512
    AgentCapabilities_AcceptsRestartCommand = 1024
    AgentCapabilities_ReportsHealth = 2048
    AgentCapabilities_ReportsRemoteConfig = 4096
    AgentCapabilities_ReportsHeartbeat = 8192
    AgentCapabilities_ReportsAvailableComponents = 16384


class RemoteConfigStatuses(IntEnum):
    RemoteConfigStatuses_UNSET = 0
    RemoteConfigStatuses_APPLIED = 1
    RemoteConfigStatuses_APPLYING = 2
    RemoteConfigStatuses_FAILED = 3


class PackageStatusEnum(IntEnum):
    """
     The status of this package.
 Status: [Beta]
    """
    PackageStatusEnum_Installed = 0
    PackageStatusEnum_InstallPending = 1
    PackageStatusEnum_Installing = 2
    PackageStatusEnum_InstallFailed = 3
    PackageStatusEnum_Downloading = 4

class AgentDescription(BaseModel):
# Attributes that identify the Agent.
# Keys/values are according to OpenTelemetry semantic conventions, see:
# https://github.com/open-telemetry/opentelemetry-specification/tree/main/specification/resource/semantic_conventions
#
# For standalone running Agents (such as OpenTelemetry Collector) the following
# attributes SHOULD be specified:
# - service.name should be set to a reverse FQDN that uniquely identifies the
#   Agent type, e.g. "io.opentelemetry.collector"
# - service.namespace if it is used in the environment where the Agent runs.
# - service.version should be set to version number of the Agent build.
# - service.instance.id should be set. It may be set equal to the Agent's
#   instance uid (equal to ServerToAgent.instance_uid field) or any other value
#   that uniquely identifies the Agent in combination with other attributes.
# - any other attributes that are necessary for uniquely identifying the Agent's
#   own telemetry.
#
# The Agent SHOULD also include these attributes in the Resource of its own
# telemetry. The combination of identifying attributes SHOULD be sufficient to
# uniquely identify the Agent's own telemetry in the destination system to which
# the Agent sends its own telemetry.
    identifying_attributes: typing.List[KeyValue] = Field(default_factory=list)
# Attributes that do not necessarily identify the Agent but help describe
# where it runs.
# The following attributes SHOULD be included:
# - os.type, os.version - to describe where the Agent runs.
# - host.* to describe the host the Agent runs on.
# - cloud.* to describe the cloud where the host is located.
# - any other relevant Resource attributes that describe this Agent and the
#   environment it runs in.
# - any user-defined attributes that the end user would like to associate
#   with this Agent.
    non_identifying_attributes: typing.List[KeyValue] = Field(default_factory=list)

class ComponentHealth(BaseModel):
    """
     The health of the Agent and sub-components
 Status: [Beta]
    """

# Set to true if the component is up and healthy.
    healthy: bool = Field(default=False)
# Timestamp since the component is up, i.e. when the component was started.
# Value is UNIX Epoch time in nanoseconds since 00:00:00 UTC on 1 January 1970.
# If the component is not running MUST be set to 0.
    start_time_unix_nano: float = Field(default=0.0)
# Human-readable error message if the component is in erroneous state. SHOULD be set
# when healthy==false.
    last_error: str = Field(default="")
# Component status represented as a string. The status values are defined by agent-specific
# semantics and not at the protocol level.
    status: str = Field(default="")
# The time when the component status was observed. Value is UNIX Epoch time in
# nanoseconds since 00:00:00 UTC on 1 January 1970.
    status_time_unix_nano: float = Field(default=0.0)
# A map to store more granular, sub-component health. It can nest as deeply as needed to
# describe the underlying system.
    component_health_map: typing.Dict[str, 'ComponentHealth'] = Field(default_factory=dict)

class AgentConfigMap(BaseModel):
# Map of configs. Keys are config file names or config section names.
# The configuration is assumed to be a collection of one or more named config files
# or sections.
# For agents that use a single config file or section the map SHOULD contain a single
# entry and the key may be an empty string.
    config_map: typing.Dict[str, 'AgentConfigFile'] = Field(default_factory=dict)

class EffectiveConfig(BaseModel):
# The effective config of the Agent.
    config_map: AgentConfigMap = Field(default_factory=AgentConfigMap)

class RemoteConfigStatus(BaseModel):
# The hash of the remote config that was last received by this Agent in the
# AgentRemoteConfig.config_hash field.
# The Server SHOULD compare this hash with the config hash
# it has for the Agent and if the hashes are different the Server MUST include
# the remote_config field in the response in the ServerToAgent message.
    last_remote_config_hash: bytes = Field(default=b"")
    status: RemoteConfigStatuses = Field(default=0)
# Optional error message if status==FAILED.
    error_message: str = Field(default="")

class PackageStatuses(BaseModel):
    """
     The PackageStatuses message describes the status of all packages that the Agent
 has or was offered.
 Status: [Beta]
    """

# A map of PackageStatus messages, where the keys are package names.
# The key MUST match the name field of PackageStatus message.
    packages: typing.Dict[str, 'PackageStatus'] = Field(default_factory=dict)
# The aggregate hash of all packages that this Agent previously received from the
# Server via PackagesAvailable message.
#
# The Server SHOULD compare this hash to the aggregate hash of all packages that
# it has for this Agent and if the hashes are different the Server SHOULD send
# an PackagesAvailable message to the Agent.
    server_provided_all_packages_hash: bytes = Field(default=b"")
# This field is set if the Agent encountered an error when processing the
# PackagesAvailable message and that error is not related to any particular single
# package.
# The field must be unset is there were no processing errors.
    error_message: str = Field(default="")

class AgentDisconnect(BaseModel):
    """
     AgentDisconnect is the last message sent from the Agent to the Server. The Server
 SHOULD forget the association of the Agent instance with the message stream.

 If the message stream is closed in the transport layer then the Server SHOULD
 forget association of all Agent instances that were previously established for
 this message stream using AgentConnect message, even if the corresponding
 AgentDisconnect message were not explicitly received from the Agent.
    """

class CertificateRequest(BaseModel):
    """
     Status: [Development]
    """

# PEM-encoded Client Certificate Signing Request (CSR), signed by client's private key.
# The Server SHOULD validate the request and SHOULD respond with a
# OpAMPConnectionSettings where the certificate.cert contains the issued
# certificate.
    csr: bytes = Field(default=b"")

class OpAMPConnectionSettingsRequest(BaseModel):
    """
     OpAMPConnectionSettingsRequest is a request for the Server to produce
 a OpAMPConnectionSettings in its response.
 Status: [Development]
    """

# A request to create a client certificate. This is used to initiate a
# Client Signing Request (CSR) flow.
# Required.
    certificate_request: CertificateRequest = Field(default_factory=CertificateRequest)

class ConnectionSettingsRequest(BaseModel):
    """
     ConnectionSettingsRequest is a request from the Agent to the Server to create
 and respond with an offer of connection settings for the Agent.
 Status: [Development]
    """

# Request for OpAMP connection settings. If this field is unset
# then the ConnectionSettingsRequest message is empty and is not actionable
# for the Server.
    opamp: OpAMPConnectionSettingsRequest = Field(default_factory=OpAMPConnectionSettingsRequest)

class CustomCapabilities(BaseModel):
# A list of custom capabilities that are supported. Each capability is a reverse FQDN
# with optional version information that uniquely identifies the custom capability
# and should match a capability specified in a supported CustomMessage.
# Status: [Development]
    capabilities: typing.List[str] = Field(default_factory=list)

class CustomMessage(BaseModel):
# A reverse FQDN that uniquely identifies the capability and matches one of the
# capabilities in the CustomCapabilities message.
# Status: [Development]
    capability: str = Field(default="")
# Type of message within the capability. The capability defines the types of custom
# messages that are used to implement the capability. The type must only be unique
# within the capability.
# Status: [Development]
    type: str = Field(default="")
# Binary data of the message. The capability must specify the format of the contents
# of the data for each custom message type it defines.
# Status: [Development]
    data: bytes = Field(default=b"")

class AvailableComponents(BaseModel):
    """
     AvailableComponents contains metadata relating to the components included
 within the agent.
 status: [Development]
    """

# A map of a unique component ID to details about the component.
# This may be omitted from the message if the server has not
# explicitly requested it be sent by setting the ReportAvailableComponents
# flag in the previous ServerToAgent message.
    components: typing.Dict[str, 'ComponentDetails'] = Field(default_factory=dict)
# Agent-calculated hash of the components.
# This hash should be included in every AvailableComponents message.
    hash: bytes = Field(default=b"")

class AgentToServer(BaseModel):
# Globally unique identifier of the running instance of the Agent. SHOULD remain
# unchanged for the lifetime of the Agent process.
# MUST be 16 bytes long and SHOULD be generated using the UUID v7 spec.
    instance_uid: bytes = Field(default=b"")
# The sequence number is incremented by 1 for every AgentToServer sent
# by the Agent. This allows the Server to detect that it missed a message when
# it notices that the sequence_num is not exactly by 1 greater than the previously
# received one.
    sequence_num: int = Field(default=0)
# Data that describes the Agent, its type, where it runs, etc.
# May be omitted if nothing changed since last AgentToServer message.
    agent_description: AgentDescription = Field(default_factory=AgentDescription)
# Bitmask of flags defined by AgentCapabilities enum.
# All bits that are not defined in AgentCapabilities enum MUST be set to 0 by
# the Agent. This allows extending the protocol and the AgentCapabilities enum
# in the future such that old Agents automatically report that they don't
# support the new capability.
# This field MUST be always set.
    capabilities: int = Field(default=0)
# The current health of the Agent and sub-components. The top-level ComponentHealth represents
# the health of the Agent overall. May be omitted if nothing changed since last AgentToServer
# message.
# Status: [Beta]
    health: ComponentHealth = Field(default_factory=ComponentHealth)
# The current effective configuration of the Agent. The effective configuration is
# the one that is currently used by the Agent. The effective configuration may be
# different from the remote configuration received from the Server earlier, e.g.
# because the Agent uses a local configuration instead (or in addition).
#
# This field SHOULD be unset if the effective config is unchanged since the last
# AgentToServer message.
    effective_config: EffectiveConfig = Field(default_factory=EffectiveConfig)
# The status of the remote config that was previously received from the Server.
# This field SHOULD be unset if the remote config status is unchanged since the
# last AgentToServer message.
    remote_config_status: RemoteConfigStatus = Field(default_factory=RemoteConfigStatus)
# The list of the Agent packages, including package statuses. This field SHOULD be
# unset if this information is unchanged since the last AgentToServer message for
# this Agent was sent in the stream.
# Status: [Beta]
    package_statuses: PackageStatuses = Field(default_factory=PackageStatuses)
# AgentDisconnect MUST be set in the last AgentToServer message sent from the
# Agent to the Server.
    agent_disconnect: AgentDisconnect = Field(default_factory=AgentDisconnect)
# Bit flags as defined by AgentToServerFlags bit masks.
    flags: int = Field(default=0)
# A request to create connection settings. This field is set for flows where
# the Agent initiates the creation of connection settings.
# Status: [Development]
    connection_settings_request: ConnectionSettingsRequest = Field(default_factory=ConnectionSettingsRequest)
# A message indicating custom capabilities supported by the Agent.
# Status: [Development]
    custom_capabilities: CustomCapabilities = Field(default_factory=CustomCapabilities)
# A custom message sent from an Agent to the Server.
# Status: [Development]
    custom_message: CustomMessage = Field(default_factory=CustomMessage)
# A message indicating the components that are available for configuration on the agent.
# Status: [Development]
    available_components: AvailableComponents = Field(default_factory=AvailableComponents)

class ComponentDetails(BaseModel):
# Extra key/value pairs that may be used to describe the component.
# The key/value pairs are according to semantic conventions, see:
# https://opentelemetry.io/docs/specs/semconv/
#
# For example, you may use the "code" semantic conventions to
# report the location of the code for a specific component:
# https://opentelemetry.io/docs/specs/semconv/attributes-registry/code/
#
# Or you may use the "vcs" semantic conventions to report the
# repository the component may be a part of:
# https://opentelemetry.io/docs/specs/semconv/attributes-registry/vcs/
    metadata: typing.List[KeyValue] = Field(default_factory=list)
# A map of component ID to sub components details. It can nest as deeply as needed to
# describe the underlying system.
    sub_component_map: typing.Dict[str, 'ComponentDetails'] = Field(default_factory=dict)

class RetryInfo(BaseModel):
    retry_after_nanoseconds: int = Field(default=0)

class ServerErrorResponse(BaseModel):
    _one_of_dict = {"ServerErrorResponse.Details": {"fields": {"retry_info"}}}
    one_of_validator = model_validator(mode="before")(check_one_of)
    type: ServerErrorResponseType = Field(default=0)
# Error message in the string form, typically human readable.
    error_message: str = Field(default="")
# Additional information about retrying if type==UNAVAILABLE.
    retry_info: RetryInfo = Field(default_factory=RetryInfo)

class AgentRemoteConfig(BaseModel):
# Agent config offered by the management Server to the Agent instance. SHOULD NOT be
# set if the config for this Agent has not changed since it was last requested (i.e.
# AgentConfigRequest.last_remote_config_hash field is equal to
# AgentConfigResponse.config_hash field).
    config: AgentConfigMap = Field(default_factory=AgentConfigMap)
# Hash of "config". The Agent SHOULD include this value in subsequent
# RemoteConfigStatus messages in the last_remote_config_hash field. This in turn
# allows the management Server to identify that a new config is available for the Agent.
#
# This field MUST be always set if the management Server supports remote configuration
# of agents.
#
# Management Server must choose a hashing function that guarantees lack of hash
# collisions in practice.
    config_hash: bytes = Field(default=b"")

class Header(BaseModel):
    """
     Status: [Beta]
    """

    key: str = Field(default="")
    value: str = Field(default="")

class Headers(BaseModel):
    """
     Status: [Beta]
    """

    headers: typing.List[Header] = Field(default_factory=list)

class TLSCertificate(BaseModel):#  The (cert,private_key) pair should be issued and signed by a Certificate
#  Authority (CA) that the destination Server recognizes.

#  It is highly recommended that the private key of the CA certificate is NOT
#  stored on the destination Server otherwise compromising the Server will allow
#  a malicious actor to issue valid Server certificates which will be automatically
#  trusted by all agents and will allow the actor to trivially MITM Agent-to-Server
#  traffic of all servers that use this CA certificate for their Server-side
#  certificates.

#  Alternatively the certificate may be self-signed, assuming the Server can
#  verify the certificate.
#     """
#      Status: [Beta]
#     """

# PEM-encoded certificate. Required.
    cert: bytes = Field(default=b"")
# PEM-encoded private key of the certificate. Required.
    private_key: bytes = Field(default=b"")
# PEM-encoded certificate of the signing CA.
# Optional. MUST be specified if the certificate is CA-signed.
# Can be stored by TLS-terminating intermediary proxies in order to verify
# the connecting client's certificate in the future.
# It is not recommended that the Agent accepts this CA as an authority for
# any purposes.
    ca_cert: bytes = Field(default=b"")

class OpAMPConnectionSettings(BaseModel):
    """
     The OpAMPConnectionSettings message is a collection of fields which comprise an
 offer from the Server to the Agent to use the specified settings for OpAMP
 connection.
 Status: [Beta]
    """

# OpAMP Server URL This MUST be a WebSocket or HTTP URL and MUST be non-empty, for
# example: "wss://example.com:4318/v1/opamp"
    destination_endpoint: str = Field(default="")
# Optional headers to use when connecting. Typically used to set access tokens or
# other authorization headers. For HTTP-based protocols the Agent should
# set these in the request headers.
# For example:
# key="Authorization", Value="Basic YWxhZGRpbjpvcGVuc2VzYW1l".
    headers: Headers = Field(default_factory=Headers)
# The Agent should use the offered certificate to connect to the destination
# from now on. If the Agent is able to validate and connect using the offered
# certificate the Agent SHOULD forget any previous client certificates
# for this connection.
# This field is optional: if omitted the client SHOULD NOT use a client-side certificate.
# This field can be used to perform a client certificate revocation/rotation.
    certificate: TLSCertificate = Field(default_factory=TLSCertificate)
# The Agent MUST periodically send an AgentToServer message if the
# AgentCapabilities_ReportsHeartbeat capability is true. At a minimum the instance_uid
# field MUST be set.
#
# An HTTP Client MUST use the value as polling interval, if heartbeat_interval_seconds is non-zero.
#
# A heartbeat is used to keep the connection active and inform the server that the Agent
# is still alive and active.
#
# If this field has no value or is set to 0, the Agent should not send any heartbeats.
# Status: [Development]
    heartbeat_interval_seconds: int = Field(default=0)

class TelemetryConnectionSettings(BaseModel):
    """
     The TelemetryConnectionSettings message is a collection of fields which comprise an
 offer from the Server to the Agent to use the specified settings for a network
 connection to report own telemetry.
 Status: [Beta]
    """

# The value MUST be a full URL an OTLP/HTTP/Protobuf receiver with path. Schema
# SHOULD begin with "https://", for example "https://example.com:4318/v1/metrics"
# The Agent MAY refuse to send the telemetry if the URL begins with "http://".
    destination_endpoint: str = Field(default="")
# Optional headers to use when connecting. Typically used to set access tokens or
# other authorization headers. For HTTP-based protocols the Agent should
# set these in the request headers.
# For example:
# key="Authorization", Value="Basic YWxhZGRpbjpvcGVuc2VzYW1l".
    headers: Headers = Field(default_factory=Headers)
# The Agent should use the offered certificate to connect to the destination
# from now on. If the Agent is able to validate and connect using the offered
# certificate the Agent SHOULD forget any previous client certificates
# for this connection.
# This field is optional: if omitted the client SHOULD NOT use a client-side certificate.
# This field can be used to perform a client certificate revocation/rotation.
    certificate: TLSCertificate = Field(default_factory=TLSCertificate)

class ConnectionSettingsOffers(BaseModel):
    """
     Status: [Beta]
    """

# Hash of all settings, including settings that may be omitted from this message
# because they are unchanged.
    hash: bytes = Field(default=b"")
# Settings to connect to the OpAMP Server.
# If this field is not set then the Agent should assume that the settings are
# unchanged and should continue using existing settings.
# The Agent MUST verify the offered connection settings by actually connecting
# before accepting the setting to ensure it does not loose access to the OpAMP
# Server due to invalid settings.
    opamp: OpAMPConnectionSettings = Field(default_factory=OpAMPConnectionSettings)
# Settings to connect to an OTLP metrics backend to send Agent's own metrics to.
# If this field is not set then the Agent should assume that the settings
# are unchanged.
#
# Once accepted the Agent should periodically send to the specified destination
# its own metrics, i.e. metrics of the Agent process and any custom metrics that
# describe the Agent state.
#
# All attributes specified in the identifying_attributes field in AgentDescription
# message SHOULD be also specified in the Resource of the reported OTLP metrics.
#
# Attributes specified in the non_identifying_attributes field in
# AgentDescription message may be also specified in the Resource of the reported
# OTLP metrics, in which case they SHOULD have exactly the same values.
#
# Process metrics MUST follow the conventions for processes:
# https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/metrics/semantic_conventions/process-metrics.md
    own_metrics: TelemetryConnectionSettings = Field(default_factory=TelemetryConnectionSettings)
# Similar to own_metrics, but for traces.
    own_traces: TelemetryConnectionSettings = Field(default_factory=TelemetryConnectionSettings)
# Similar to own_metrics, but for logs.
    own_logs: TelemetryConnectionSettings = Field(default_factory=TelemetryConnectionSettings)
# Another set of connection settings, with a string name associated with each.
# How the Agent uses these is Agent-specific. Typically the name represents
# the name of the destination to connect to (as it is known to the Agent).
# If this field is not set then the Agent should assume that the other_connections
# settings are unchanged.
    other_connections: typing.Dict[str, 'OtherConnectionSettings'] = Field(default_factory=dict)

class PackagesAvailable(BaseModel):
    """
     List of packages that the Server offers to the Agent.
 Status: [Beta]
    """

# Map of packages. Keys are package names, values are the packages available for download.
    packages: typing.Dict[str, 'PackageAvailable'] = Field(default_factory=dict)
# Aggregate hash of all remotely installed packages. The Agent SHOULD include this
# value in subsequent PackageStatuses messages. This in turn allows the management
# Server to identify that a different set of packages is available for the Agent
# and specify the available packages in the next ServerToAgent message.
#
# This field MUST be always set if the management Server supports packages
# of agents.
#
# The hash is calculated as an aggregate of all packages names and content.
    all_packages_hash: bytes = Field(default=b"")

class AgentIdentification(BaseModel):
    """
     Properties related to identification of the Agent, which can be overridden
 by the Server if needed
    """

# When new_instance_uid is set, Agent MUST update instance_uid
# to the value provided and use it for all further communication.
# MUST be 16 bytes long and SHOULD be generated using the UUID v7 spec.
    new_instance_uid: bytes = Field(default=b"")

class ServerToAgentCommand(BaseModel):
    """
     ServerToAgentCommand is sent from the Server to the Agent to request that the Agent
 perform a command.
 Status: [Beta]
    """

    type: CommandType = Field(default=0)

class ServerToAgent(BaseModel):
# Agent instance uid. MUST match the instance_uid field in AgentToServer message.
# Used for multiplexing messages from/to multiple agents using one message stream.
    instance_uid: bytes = Field(default=b"")
# error_response is set if the Server wants to indicate that something went wrong
# during processing of an AgentToServer message. If error_response is set then
# all other fields below must be unset and vice versa, if any of the fields below is
# set then error_response must be unset.
    error_response: ServerErrorResponse = Field(default_factory=ServerErrorResponse)
# remote_config field is set when the Server has a remote config offer for the Agent.
    remote_config: AgentRemoteConfig = Field(default_factory=AgentRemoteConfig)
# This field is set when the Server wants the Agent to change one or more
# of its client connection settings (destination, headers, certificate, etc).
# Status: [Beta]
    connection_settings: ConnectionSettingsOffers = Field(default_factory=ConnectionSettingsOffers)
# This field is set when the Server has packages to offer to the Agent.
# Status: [Beta]
    packages_available: PackagesAvailable = Field(default_factory=PackagesAvailable)
# Bit flags as defined by ServerToAgentFlags bit masks.
    flags: int = Field(default=0)
# Bitmask of flags defined by ServerCapabilities enum.
# All bits that are not defined in ServerCapabilities enum MUST be set to 0
# by the Server. This allows extending the protocol and the ServerCapabilities
# enum in the future such that old Servers automatically report that they
# don't support the new capability.
# This field MUST be set in the first ServerToAgent sent by the Server and MAY
# be omitted in subsequent ServerToAgent messages by setting it to
# UnspecifiedServerCapability value.
    capabilities: int = Field(default=0)
# Properties related to identification of the Agent, which can be overridden
# by the Server if needed.
    agent_identification: AgentIdentification = Field(default_factory=AgentIdentification)
# Allows the Server to instruct the Agent to perform a command, e.g. RESTART. This field should not be specified
# with fields other than instance_uid and capabilities. If specified, other fields will be ignored and the command
# will be performed.
# Status: [Beta]
    command: ServerToAgentCommand = Field(default_factory=ServerToAgentCommand)
# A message indicating custom capabilities supported by the Server.
# Status: [Development]
    custom_capabilities: CustomCapabilities = Field(default_factory=CustomCapabilities)
# A custom message sent from the Server to an Agent.
# Status: [Development]
    custom_message: CustomMessage = Field(default_factory=CustomMessage)

class OtherConnectionSettings(BaseModel):
    """
     The OtherConnectionSettings message is a collection of fields which comprise an
 offer from the Server to the Agent to use the specified settings for a network
 connection. It is not required that all fields in this message are specified.
 The Server may specify only some of the fields, in which case it means that
 the Server offers the Agent to change only those fields, while keeping the
 rest of the fields unchanged.

 For example the Server may send a ConnectionSettings message with only the
 certificate field set, while all other fields are unset. This means that
 the Server wants the Agent to use a new certificate and continue sending to
 the destination it is currently sending using the current header and other
 settings.

 For fields which reference other messages the field is considered unset
 when the reference is unset.

 For primitive field (string) we rely on the "flags" to describe that the
 field is not set (this is done to overcome the limitation of old protoc
 compilers don't generate methods that allow to check for the presence of
 the field.
 Status: [Beta]
    """

# A URL, host:port or some other destination specifier.
    destination_endpoint: str = Field(default="")
# Optional headers to use when connecting. Typically used to set access tokens or
# other authorization headers. For HTTP-based protocols the Agent should
# set these in the request headers.
# For example:
# key="Authorization", Value="Basic YWxhZGRpbjpvcGVuc2VzYW1l".
    headers: Headers = Field(default_factory=Headers)
# The Agent should use the offered certificate to connect to the destination
# from now on. If the Agent is able to validate and connect using the offered
# certificate the Agent SHOULD forget any previous client certificates
# for this connection.
# This field is optional: if omitted the client SHOULD NOT use a client-side certificate.
# This field can be used to perform a client certificate revocation/rotation.
    certificate: TLSCertificate = Field(default_factory=TLSCertificate)
# Other connection settings. These are Agent-specific and are up to the Agent
# interpret.
    other_settings: typing.Dict[str, str] = Field(default_factory=dict)

class DownloadableFile(BaseModel):
    """
     Status: [Beta]
    """

# The URL from which the file can be downloaded using HTTP GET request.
# The Server at the specified URL SHOULD support range requests
# to allow for resuming downloads.
    download_url: str = Field(default="")
# The hash of the file content. Can be used by the Agent to verify that the file
# was downloaded correctly.
    content_hash: bytes = Field(default=b"")
# Optional signature of the file content. Can be used by the Agent to verify the
# authenticity of the downloaded file, for example can be the
# [detached GPG signature](https://www.gnupg.org/gph/en/manual/x135.html#AEN160).
# The exact signing and verification method is Agent specific. See
# https://github.com/open-telemetry/opamp-spec/blob/main/specification.md#code-signing
# for recommendations.
    signature: bytes = Field(default=b"")
# Optional headers to use when downloading a file. Typically used to set
# access tokens or other authorization headers. For HTTP-based protocols
# the Agent should set these in the request headers.
# For example:
# key="Authorization", Value="Basic YWxhZGRpbjpvcGVuc2VzYW1l".
# Status: [Development]
    headers: Headers = Field(default_factory=Headers)

class PackageAvailable(BaseModel):
    """
     Each Agent is composed of one or more packages. A package has a name and
 content stored in a file. The content of the files, functionality
 provided by the packages, how they are stored and used by the Agent side is Agent
 type-specific and is outside the concerns of the OpAMP protocol.

 If the Agent does not have an installed package with the specified name then
 it SHOULD download it from the specified URL and install it.

 If the Agent already has an installed package with the specified name
 but with a different hash then the Agent SHOULD download and
 install the package again, since it is a different version of the same package.

 If the Agent has an installed package with the specified name and the same
 hash then the Agent does not need to do anything, it already
 has the right version of the package.
 Status: [Beta]
    """

    type: PackageType = Field(default=0)
# The package version that is available on the Server side. The Agent may for
# example use this information to avoid downloading a package that was previously
# already downloaded and failed to install.
    version: str = Field(default="")
# The downloadable file of the package.
    file: DownloadableFile = Field(default_factory=DownloadableFile)
# The hash of the package. SHOULD be calculated based on all other fields of the
# PackageAvailable message and content of the file of the package. The hash is
# used by the Agent to determine if the package it has is different from the
# package the Server is offering.
    hash: bytes = Field(default=b"")

class PackageDownloadDetails(BaseModel):
    """
     Additional details that an agent can use to describe an in-progress package download.
 Status: [Development]
    """

# The package download progress as a percentage.
    download_percent: float = Field(default=0.0)
# The current package download rate in bytes per second.
    download_bytes_per_second: float = Field(default=0.0)

class PackageStatus(BaseModel):
    """
     The status of a single package.
 Status: [Beta]
    """

# Package name. MUST be always set and MUST match the key in the packages field
# of PackageStatuses message.
    name: str = Field(default="")
# The version of the package that the Agent has.
# MUST be set if the Agent has this package.
# MUST be empty if the Agent does not have this package. This may be the case
# for example if the package was offered by the Server but failed to install
# and the Agent did not have this package previously.
    agent_has_version: str = Field(default="")
# The hash of the package that the Agent has.
# MUST be set if the Agent has this package.
# MUST be empty if the Agent does not have this package. This may be the case for
# example if the package was offered by the Server but failed to install and the
# Agent did not have this package previously.
    agent_has_hash: bytes = Field(default=b"")
# The version of the package that the Server offered to the Agent.
# MUST be set if the installation of the package is initiated by an earlier offer
# from the Server to install this package.
#
# MUST be empty if the Agent has this package but it was installed locally and
# was not offered by the Server.
#
# Note that it is possible for both agent_has_version and server_offered_version
# fields to be set and to have different values. This is for example possible if
# the Agent already has a version of the package successfully installed, the Server
# offers a different version, but the Agent fails to install that version.
    server_offered_version: str = Field(default="")
# The hash of the package that the Server offered to the Agent.
# MUST be set if the installation of the package is initiated by an earlier
# offer from the Server to install this package.
#
# MUST be empty if the Agent has this package but it was installed locally and
# was not offered by the Server.
#
# Note that it is possible for both agent_has_hash and server_offered_hash
# fields to be set and to have different values. This is for example possible if
# the Agent already has a version of the package successfully installed, the
# Server offers a different version, but the Agent fails to install that version.
    server_offered_hash: bytes = Field(default=b"")
    status: PackageStatusEnum = Field(default=0)
# Error message if the status is erroneous.
    error_message: str = Field(default="")
# Optional details that may be of interest to a user.
# Should only be set if status is Downloading.
# Status: [Development]
    download_details: PackageDownloadDetails = Field(default_factory=PackageDownloadDetails)

class AgentConfigFile(BaseModel):
# Config file or section body. The content, format and encoding depends on the Agent
# type. The content_type field may optionally describe the MIME type of the body.
    body: bytes = Field(default=b"")
# Optional MIME Content-Type that describes what's in the body field, for
# example "text/yaml".
    content_type: str = Field(default="")
