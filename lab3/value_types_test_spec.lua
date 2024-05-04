local busted = require("busted")
local assert = require("luassert")

local function increase(val)
    val = val + 1
    return val
end

describe("Value Type Test", function()
    it("Should check if Lua variables are value types", function()
        local num = 5

        increase(num)

        assert.is_true(num == 5)
    end)
end)